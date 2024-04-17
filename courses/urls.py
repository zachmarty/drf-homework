from django.urls import path
from rest_framework.routers import DefaultRouter
from courses.apps import CoursesConfig
from courses.views import (
    CourseViewSet,
    LessonCreateView,
    LessonDeleteView,
    LessonDetailView,
    LessonListView,
    LessonUpdateView,
)


app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r"courses", CourseViewSet, basename="courses")

urlpatterns = [
    path("lessons", LessonListView.as_view(), name="lessons"),
    path("lesson/<int:pk>", LessonDetailView.as_view(), name="lesson_detail"),
    path("lesson/create", LessonCreateView.as_view(), name="lesson_create"),
    path("lesson/<int:pk>/update", LessonUpdateView.as_view(), name="lesson_update"),
    path("lesson/<int:pk>/delete", LessonDeleteView.as_view(), name="lesson_delete"),
] + router.urls
