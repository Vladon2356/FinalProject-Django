from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    age = models.SmallIntegerField(verbose_name="Age", null=True)
