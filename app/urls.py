from django.urls import  path
from .views import *
# urlpatterns=[
#     path('makepost/',newpost,name='newpost'),
#     path('messages/',messages,name='messages'),
#     path('messages/<str:pk>/',get_messages,name= "get_messages"),
#     path('getmessage/<str:pk>/',get_message,name= "get_message"),
#     path('send/',sendMessage,name ='send'),
#     path('sendreq/<str:pk>/',sendrequest,name='sendmsgrequest'),
#     path('sendRequest/<str:pk>/',sendrequestPost,name='sendrequest'),
#     path('getpostmessage/<str:pk>/',getpost_message,name='getpost_message'),
#     path('ownposts/',ownposts,name='ownposts'),
#     path('delete/<str:pk>/',deletepost,name='deletepost'),
#     path('edituserprofile/',editProfile,name='editProfile'),
#     path('vewpostdeatils/<str:pk>/',viewpostdetails,name='viewpostdetails'),
#     path('search/',search,name='search'),
#     path('notloginsearch/',notloginsearch,name='notloginsearch')
# ]

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path("sign-up-steps/", SignUpSteps, name="sign_up_steps"),
    path('contact/', contact, name='contact'),
    path('blog/', blog, name='blog'),
    path('blog-single/', blog_single, name='blog-single'),
    path('faqs/', faqs, name='faqs'),
]