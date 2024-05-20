from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    city = models.TextField()
    state = models.TextField()
    zip_code = models.TextField()
    skills = models.CharField(max_length=256, blank=True)  # Comma separated list of skills
    skills_range= models.CharField(max_length=256, blank=True)
    websitelinks = models.CharField(max_length=256, default=',,,,')
    role = models.CharField(max_length=256, default='Fresher') 
    experience=models.CharField(max_length=256, blank=True)
    full_name=models.CharField(max_length=100, blank=True)