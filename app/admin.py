from django.contrib import admin
from .models import Postings,Message,Chatbox,Appliedfor

# Register your models here.
admin.site.register(Postings)
admin.site.register(Message)
admin.site.register(Chatbox)
admin.site.register(Appliedfor)