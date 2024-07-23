from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    full_name=models.CharField(max_length=100)
    role = models.CharField(max_length=100, default='Fresher')
    sector = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    cv = models.FileField(upload_to='cv/',null=True,blank=True)
    skills_expertise = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', default='../static/theme-assets/images/avatar/05.jpg', blank=True, null=True)


class Review(models.Model):
    reviewer = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='given_reviews', null=True, blank=True)
    reviewed_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='received_reviews', null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    rating = models.CharField(max_length=5, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.reviewer.full_name} for {self.reviewed_user.full_name}" if self.reviewer and self.reviewed_user else "Anonymous Review"