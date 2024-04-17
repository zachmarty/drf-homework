from django.contrib import admin

from courses.models import Course, Lesson


# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "preview")
    list_filter = ("name",)
    search_fields = ("name", "description")


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "course")
    list_filter = ("name", "course")
    search_fields = ("name", "course")
