from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None
    email = models.EmailField(
        unique=True, verbose_name="Email", help_text="Email address"
    )
    phone = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        verbose_name="Phone",
        help_text="Phone number",
    )
    city = models.CharField(
        max_length=11, blank=True, null=True, verbose_name="City", help_text="City"
    )
    avatar = models.ImageField(
        upload_to="users/avatars/",
        blank=True,
        null=True,
        verbose_name="Avatar",
        help_text="Avatar",
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

