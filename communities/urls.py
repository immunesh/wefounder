from django.urls import  path
from . import views
urlpatterns = [
    path('community/', views.Community, name='community'),
    path('community-single/', views.communitySingle, name='community_single'),
]