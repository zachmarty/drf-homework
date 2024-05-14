from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, max_length=100, verbose_name="Почта")
    phone = models.CharField(
        max_length=30, verbose_name="Телефон", blank=True, null=True
    )
    city = models.CharField(max_length=50, verbose_name="Город", blank=True, null=True)
    avatar = models.ImageField(verbose_name="Картинка", blank=True, null=True)
    last_login = models.DateTimeField(
        verbose_name="Последний вход", blank=True, null=True, default=datetime.now()
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
        ordering = [
            "id",
        ]
