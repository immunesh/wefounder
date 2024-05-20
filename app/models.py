from django.db import models
from user_account.models import CustomUser

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