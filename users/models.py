from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    email = models.EmailField(
        unique=True,
        verbose_name="Почта"
    )
    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name="Номер телефона"
    )
    avatar = models.ImageField(
        upload_to="users/avatars",
        blank=True,
        null=True,
        verbose_name="Аватарка"
    )
    chat_id = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name="chat_id"
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
