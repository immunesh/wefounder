from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    full_name=models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='Fresher')
    company = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    looking_for = models.CharField(max_length=200)
    i_can = models.CharField(max_length=200, default='')
    skills_expertise = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', default='../static/theme-assets/images/avatar/05.jpg', blank=True, null=True)