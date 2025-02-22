from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Customer(AbstractUser):
    phone = models.CharField(max_length=10, blank=True, null=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)
