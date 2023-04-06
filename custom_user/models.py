from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    street_address = models.CharField(max_length=100)
    street_address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=25)
    zip_code = models.CharField(max_length=15)
    phone = models.CharField(max_length=25)
    birthday = models.DateField(default=timezone.now)
    biography = models.TextField()
    facebook = models.CharField(max_length=250, blank=True)
    twitter = models.CharField(max_length=250, blank=True)
    instagram = models.CharField(max_length=250, blank=True)
    linkedin = models.CharField(max_length=250, blank=True)

    def __str__(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        else:
            return self.username
