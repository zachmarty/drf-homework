from rest_framework import serializers

from courses.models import Course, Lesson, Payment
from courses.validators import LessonValidator


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = "__all__"
        validators = [LessonValidator(field="video")]


class CourseSerializer(serializers.ModelSerializer):

    # lesson_count = serializers.IntegerField(source="lesson_set.all.count")
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source="lesson_set", many=True, read_only=True)

    class Meta:
        model = Course
        fields = "__all__"
        

    def get_lesson_count(self, instance):
        if instance.lesson_set.all().count():
            return instance.lesson_set.all().count()
        return 0


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = "__all__"
