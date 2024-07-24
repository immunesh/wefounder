from django.contrib import admin
from .models import CommunityCategory, CommunityPost

@admin.register(CommunityCategory)
class CommunityCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}
    ordering = ('name',)
    
# @admin.register(Sector)
# class SectorAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)
#     # prepopulated_fields = {'slug': ('name',)}
#     ordering = ('name',)
    
# @admin.register(SubSector)
# class CommunityCategoryAdmin(admin.ModelAdmin):
#     list_display = ('name',)
#     search_fields = ('name',)
#     # prepopulated_fields = {'slug': ('name',)}
#     ordering = ('name',)

@admin.register(CommunityPost)
class CommunityPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'slug', 'created_at', 'updated_at')
    search_fields = ('title', 'user__username', 'category_name', 'description')
    list_filter = ('category', 'user')
    ordering = ('title',)
    raw_id_fields = ('user','category')
    prepopulated_fields = {'slug': ('title',)}


    