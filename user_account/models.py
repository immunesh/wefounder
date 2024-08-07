from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    full_name=models.CharField(max_length=100,blank=False, null=False)
    role = models.CharField(max_length=100, default='Fresher')
    sector = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    cv = models.FileField(upload_to='cv/',null=True,blank=True)
    skills_expertise = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', default='../static/theme-assets/images/avatar/05.jpg', blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.username
    
     
class Review(models.Model):
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='given_reviews', null=True, blank=True)
    reviewed_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_reviews', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    rating = models.CharField(max_length=5, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer.full_name} for {self.reviewed_user.full_name}" if self.reviewer and self.reviewed_user else "Anonymous Review"
    
class Room(models.Model):
    name = models.CharField(max_length=255)
    slug=models.SlugField(max_length=200,default='slug')
    
    def __str__(self):
        return self.name

class Message(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)