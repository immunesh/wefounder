from django.db import models
from user_account.models import CustomUser
from django.urls import reverse


# Create your models here.
class Postings(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    investment_needed=models.TextField()
    typeofpost=models.CharField(max_length=128,default='')
    location=models.CharField(max_length=256,default='')
    company_name=models.CharField(max_length=256,default='')
    website=models.CharField(max_length=256,default='')
    duration = models.TextField()
    skills=models.TextField()
    createdTime=models.DateTimeField(auto_now_add=True)
    creator=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="posting")

    def  __str__(self):
        return self.title
    
class Message(models.Model):
    sender = models.ForeignKey(CustomUser,related_name='sender',on_delete=models.CASCADE)
    receiver = models.ForeignKey(CustomUser,related_name="receiver",on_delete=models.CASCADE)
    message = models.TextField()
    contact=models.ForeignKey('Chatbox',on_delete=models.CASCADE)
    createdTime=models.DateTimeField(auto_now_add=True)
    def __stt__  (self):
        return self.message
    
class Chatbox(models.Model):
    sender=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name='cont_sender')
    receiver=models.ForeignKey(CustomUser,on_delete=models.CASCADE, related_name='cont_reciever')
    def __int__(self):
        return self.id
    
class Appliedfor(models.Model):
    applicants=models.ManyToManyField(CustomUser)
    applied=models.BooleanField(default=False)
    post=models.ForeignKey(Postings,on_delete=models.CASCADE)

# Custom model our


class Subscribe(models.Model):
    email = models.EmailField(max_length=150)


class Review(models.Model):
    name = models.CharField(max_length=80)
    Contact = models.IntegerField()
    rating = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)


class Faq(models.Model):
    # id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=450, null=False)
    answer = models.CharField(max_length=500, null = False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Contact(models.Model):
    name = models.CharField(max_length=75)
    # email = models.ForeignKey(Subscribe, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150, null=False)
    phone = models.IntegerField(null=False)
    company = models.CharField(max_length=50)
    Message = models.CharField(max_length=1500, null=False)










