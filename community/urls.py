from django.urls import  path
from . import views
urlpatterns = [
    path('community/', views.Community, name='community'),
    # path('account/@<str:username>/', views.userProfile, name='viewProfile'),
]