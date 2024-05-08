from django.contrib import admin

from courses.models import Course, Lesson, Payment, Sub


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview", "user")
    list_filter = ("name",)
    search_fields = ("name", "description")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course", "user")
    list_filter = ("name", "course")
    search_fields = ("name", "course")


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "pay_date", "lesson", "course", "payment", "method")
    list_filter = ("id", "pay_date", "user", "payment")
    search_fields = ("id", "pay_date", "user", "payment")


@admin.register(Sub)
class SubAdmin(admin.ModelAdmin):
    list_display = ("user", "course")
    list_filter = ("id", "user", "course")
    search_fields = ("user", "course")
