from django.contrib import admin
from .models import Subscribe, Review, Faq, Contact

@admin.register(Subscribe)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('email',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'Contact', 'rating', 'created_at')
    search_fields = ('name', 'Contact')
    list_filter = ('rating', 'created_at')

@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer', 'created_at', 'updated_at')
    search_fields = ('question', 'answer')
    list_filter = ('created_at', 'updated_at')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'company', 'Message')
    search_fields = ('name', 'email', 'phone', 'company')
    list_filter = ('company',)
