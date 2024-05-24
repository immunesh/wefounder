from django.contrib import admin

from .models import Postings, Message, Chatbox, Appliedfor, Subscribe, Review, Faq, Contact




# Register your models here.
admin.site.register(Postings)
admin.site.register(Message)
admin.site.register(Chatbox)
admin.site.register(Appliedfor)

admin.site.register(Subscribe)
admin.site.register(Review)
admin.site.register(Faq)
admin.site.register(Contact)





