from django.contrib import admin
from django.urls import path,include

urlpatterns = [ 
    path('',include("app.urls")), # Main
    path('admin/',include('customadmin.urls')),
    path('djadmin/', admin.site.urls),
]