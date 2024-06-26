from tabnanny import verbose
from django.db import models
from users.models import User


class Course(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    last_update = models.DateTimeField(
        verbose_name="Последнее обновление",
        blank=True,
        null=True,
    )
    preview = models.ImageField(verbose_name="Картинка", blank=True, null=True)
    description = models.TextField(
        max_length=500, blank=True, null=True, verbose_name="Описание"
    )
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
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
    video = models.URLField(verbose_name="Видео", blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    user = models.ForeignKey(
        User,
        null=True,
        blank=True,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"
        ordering = [
            "name",
        ]

    def __str__(self) -> str:
        return f"{self.name}"


class Payment(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        blank=True,
        null=True,
    )
    pay_date = models.DateTimeField(verbose_name="Дата оплаты", blank=True, null=True)
    lesson = models.ForeignKey(
        Lesson,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный урок",
        blank=True,
        null=True,
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name="Оплаченный курс",
        blank=True,
        null=True,
    )
    payment = models.FloatField(verbose_name="Сумма оплаты", default=0)
    method = models.CharField(
        verbose_name="Метод оплаты", default="карта", max_length=10
    )
    payment_url = models.URLField(
        verbose_name="Ссылка на оплату", blank=True, null=True, max_length=500
    )
    session_id = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Айди ссессии"
    )

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"
        ordering = [
            "user",
            "-pay_date",
        ]

    def __str__(self) -> str:
        return f"{self.user} {self.payment}"


class Sub(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = [
            "id",
        ]
