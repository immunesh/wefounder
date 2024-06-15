from django.urls import  path
from . import views
urlpatterns = [
    path('community/', views.Community, name='community'),
    path('community/<slug:slug>/', views.CommunitySingle.as_view(), name='community_single'),

]