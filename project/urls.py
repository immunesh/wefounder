from django.contrib import admin
from django.urls import path,include

urlpatterns = [ 
    path('',include("app.urls")),
    path('',include("user_account.urls")),
    # path('admin/',include('customadmin.urls')),
    path('admin/', admin.site.urls),
]