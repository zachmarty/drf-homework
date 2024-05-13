import datetime
from django.http import HttpResponseRedirect
from rest_framework.reverse import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
import stripe
from config import settings
from courses.models import Course, Lesson, Payment, Sub
from courses.paginators import CoursePaginator, LessonPaginator
from courses.payment_modules import create_payment_price, create_payment_product, create_payment_session, get_session_info
from courses.permissions import IsModer, IsUserOrStaff
from courses.serializers import CourseSerializer, LessonSerializer, PaymentSerializer
from django.shortcuts import get_object_or_404

stripe.api_key = settings.STRIPE_API_KEY


class PaymentListView(ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ["lesson", "course", "method"]
    ordering_fields = [
        "pay_date",
    ]


class CourseViewSet(ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "create":
            self.permission_classes = [
                IsAuthenticated,
                ~IsModer,
            ]  # Модер не может создавать
        elif self.action == "update":
            self.permission_classes = [
                IsAuthenticated,
                IsUserOrStaff | IsModer,
            ]  # Пользователь должен быть зареган + быть владельцем,
            # админом или модером
        elif self.action == "destroy":
            self.permission_classes = [
                IsUserOrStaff,
                IsAuthenticated,
            ]
        return [permission() for permission in self.permission_classes]

    def create(self, request, *args, **kwargs):
        data = request.data
        new_course = Course.objects.create(**data, user=self.request.user)
        new_course.save()
        instance = CourseSerializer(new_course)

        return Response(instance.data)


class LessonDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]
    pagination_class = LessonPaginator


class LessonCreateView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [
        IsAuthenticated,
        ~IsModer,
    ]

    def perform_create(self, serializer):
        new_lesson = serializer.save()
        new_lesson.user = self.request.user
        new_lesson.save()


class LessonUpdateView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, IsModer | IsUserOrStaff]


class LessonDeleteView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsUserOrStaff, IsAuthenticated]


class SubCreateView(RetrieveAPIView):
    serializer_class = Sub
    queryset = Sub.objects.all()
    permission_classes = [IsAuthenticated]

    def post(self, *args, **kwargs):
        user = self.request.user
        course_id = self.request.data["course"]
        course = get_object_or_404(Course, id=course_id)
        if Sub.objects.filter(user=user, course=course).exists():
            sub = Sub.objects.get(user=user, course=course).delete()
            message = f"Подписка на курс {course.name} отменена"
        else:
            sub = Sub.objects.create(user=user, course=course)
            sub.save()
            message = f"Вы подписались на курс {course.name}"
        return Response({"message": message})


class PaymentCreateView(CreateAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_payment = serializer.save()
        new_payment.user = self.request.user
        type = "course" in self.request.get_full_path()
        if type:
            pay_course = Course.objects.get(id=self.kwargs["pk"])
            new_payment.course = pay_course
            amount = len(list(Lesson.objects.filter(course=pay_course))) * 1000
            new_payment.payment = amount
            prod = create_payment_product(pay_course.name, pay_course.description)
            price = create_payment_price(amount, prod["id"])
            session = create_payment_session(price["id"], new_payment.id, self.request)
            new_payment.payment_url = session["url"]
            new_payment.session_id = session["id"]
            new_payment.pay_date = datetime.datetime.now()
            new_payment.save()
            return HttpResponseRedirect(redirect_to=session["url"])

        else:
            pay_lesson = Lesson.objects.get(id=self.kwargs["pk"])
            new_payment.lesson = pay_lesson
            new_payment.payment = 1000
            prod = create_payment_product(pay_lesson.name, pay_lesson.description)
            price = create_payment_price(new_payment.payment, prod['id'])
            session = create_payment_session(price["id"], new_payment.id, self.request)
            new_payment.payment_url = session["url"]
            new_payment.session_id = session["id"]
            new_payment.pay_date = datetime.datetime.now()
            new_payment.save()
            return HttpResponseRedirect(redirect_to=session["url"])


class PaymentRetrieveView(RetrieveAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = [IsAuthenticated, IsUserOrStaff]

    def get(self, request, *args, **kwargs):
        payment = self.get_object()
        session = get_session_info(payment.session_id)
        if session.status == "complete":
            return Response({
                'message':'Оплата прошла успешно'
            })
        else:
            return Response({
                'message':'Оплата не получена',
                'pay_url':session.url
            })