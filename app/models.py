from django.db import models
# Create your models here.

class Subscribe(models.Model):
    email = models.EmailField(max_length=150)
    def __str__(self):
        return self.email

class Review(models.Model):
    name = models.CharField(max_length=80)
    Contact = models.IntegerField()
    rating = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Faq(models.Model):
    question = models.CharField(max_length=450, null=False)
    answer = models.CharField(max_length=500, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.question

class Contact(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField(max_length=150, null=False)
    phone = models.IntegerField(null=False)
    company = models.CharField(max_length=50)
    Message = models.CharField(max_length=1500, null=False)
    
    def __str__(self):
        return self.name