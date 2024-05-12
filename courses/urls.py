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
    PaymentListView,
    PaymentRetrieveView,
    SubCreateView,
    PaymentCreateView,
)


app_name = CoursesConfig.name

router = DefaultRouter()
router.register(r"course", CourseViewSet, basename="course")

urlpatterns = [
    path("lesson", LessonListView.as_view(), name="lesson_list"),
    path("lesson/<int:pk>", LessonDetailView.as_view(), name="lesson_detail"),
    path("lesson/create", LessonCreateView.as_view(), name="lesson_create"),
    path("lesson/<int:pk>/update", LessonUpdateView.as_view(), name="lesson_update"),
    path("lesson/<int:pk>/delete", LessonDeleteView.as_view(), name="lesson_delete"),
    path(
        "lesson/<int:pk>/pay", PaymentCreateView.as_view(), name="lesson_payment_create"
    ),
    path(
        "course/<int:pk>/pay", PaymentCreateView.as_view(), name="course_payment_create"
    ),
    path("payment/", PaymentListView.as_view(), name="payment_list"),
    path("payment/<int:pk>", PaymentRetrieveView.as_view(), name="payment_detail"),
    path("sub", SubCreateView.as_view(), name="sub"),
] + router.urls
