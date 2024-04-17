from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
)
from rest_framework.viewsets import ModelViewSet

from courses.models import Course, Lesson
from courses.serializers import CourseSerializer, LessonSerializer


class CourseViewSet(ModelViewSet):
    serializer_class = LessonSerializer
    queryset = Course.objects.all()


class LessonDetailView(RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonListView(ListAPIView):
    serializer_class = LessonSerializer
    queryset = Course.objects.all()


class LessonCreateView(CreateAPIView):
    serializer_class = LessonSerializer
    queryset = Course.objects.all()


class LessonUpdateView(UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Course.objects.all()


class LessonDeleteView(DestroyAPIView):
    serializer_class = LessonSerializer
    queryset = Course.objects.all()
