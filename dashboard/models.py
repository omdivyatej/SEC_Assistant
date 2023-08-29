from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    # User Identification
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Personal Information
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    # Contact Information
    email = models.EmailField(null=True, blank=True)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    # User Activity and History
    last_login = models.DateTimeField(null=True, blank=True)
    signup_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username