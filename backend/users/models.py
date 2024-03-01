from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(blank=False, max_length=25, verbose_name="email address")

    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"

    def __str__(self):
        return self.get_full_name()

    class Meta:
        verbose_name = ('User')
        verbose_name_plural = ('Users')