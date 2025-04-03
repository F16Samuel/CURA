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
    

    from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Consultation(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    previous_history = models.TextField(blank=True, null=True)
    symptoms = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Consultation for {self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"