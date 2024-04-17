from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    preview = models.ImageField(verbose_name="Картинка", blank=True, null=True)
    description = models.TextField(
        max_length=500, blank=True, null=True, verbose_name="Описание"
    )

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"
        ordering = [
            "name",
        ]

    def __str__(self) -> str:
        return f"{self.name}"


class Lesson(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(
        max_length=500, verbose_name="Описание", blank=True, null=True
    )
    preview = models.ImageField(verbose_name="Картинка", blank=True, null=True)
    video = models.URLField(verbose_name="Видео")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = [
            "name",
        ]

    def __str__(self) -> str:
        return f"{self.name} {self.course}"
