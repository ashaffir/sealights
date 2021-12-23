from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    last_name = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )

    def __str__(self):
        return str(self.email)
