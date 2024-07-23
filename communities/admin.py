from django.contrib import admin
from .models import CommunityCategory, CommunityPost

@admin.register(CommunityCategory)
class CommunityCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)

@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'role', 'sector', 'sub_sector','pdf', 'slug', 'created_at', 'updated_at')
    search_fields = ('title', 'user__username', 'description')
    list_filter = ('role', 'user')
    ordering = ('title',)
    raw_id_fields = ('user',)
    prepopulated_fields = {'slug': ('title',)}