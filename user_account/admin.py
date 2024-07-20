from django.contrib import admin
from .models import CustomUser, Review


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'role')
    search_fields = ('username', 'full_name', 'email')



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('reviewer', 'reviewed_user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('reviewer__full_name', 'reviewed_user__full_name', 'content')
    raw_id_fields = ('reviewer', 'reviewed_user')
