from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import permission_classes
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

from courses.models import Course, Lesson, Payment
from courses.permissions import IsModer, IsUserOrStaff
from courses.serializers import CourseSerializer, LessonSerializer, PaymentSerializer


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
    
    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "retrieve":
            self.permission_classes = [IsAuthenticated]
        elif self.action == "create":
            self.permission_classes = [IsAuthenticated, ~IsModer]#Модер не может создавать
        elif self.action == "update":
            self.permission_classes = [IsAuthenticated, IsUserOrStaff | IsModer]#Пользователь должен быть зареган + быть владельцем, 
            #админом или модером
        elif self.action == "destroy":
            self.permission_classes = [IsUserOrStaff, IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def create(self, request, *args, **kwargs):
        data = request.data
        instance = CourseSerializer(data = data)
        instance.user = self.request.user
        instance.is_valid(raise_exception=True)
        instance.save()
        return Response(instance.data)
        


class LessonDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated]


class LessonCreateView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsAuthenticated, ~IsModer]

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
