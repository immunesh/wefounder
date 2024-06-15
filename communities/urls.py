from django.urls import  path
from . import views
urlpatterns = [
    path('communities/', views.Community, name='communities'),
    path('community/<slug:slug>/', views.CommunitySingle.as_view(), name='community_single'),
]