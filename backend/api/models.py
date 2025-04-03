from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    hospital = models.CharField(max_length=255, blank=True, null=True)  # Only for doctors

    def __str__(self):
        return self.username
