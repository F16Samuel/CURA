from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
    hospital = models.CharField(max_length=255, blank=True, null=True)  # Allow hospital to be optional
    email = models.EmailField(unique=True)  # Ensure email is unique

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # Keep username for uniqueness

    def __str__(self):
        return f"{self.email} - {self.role}"