from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    GENDER_CHOISES = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    phone_number = models.CharField(max_length=14, unique=True, blank=True, null=True)
    image = models.ImageField(upload_to='users/', blank=True, null=True)
    middle_name = models.CharField(max_length=255, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True, choices=GENDER_CHOISES)
    address = models.TextField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.username
