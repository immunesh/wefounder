from django.urls import path
from .views import blog, BlogSingle, category, tag

urlpatterns = [
    path('blogs/', blog, name='blogs'),
    path('<slug:slug>/', BlogSingle.as_view(), name='blog_single'),
]