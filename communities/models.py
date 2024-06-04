from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from user_account.models import CustomUser

class CommunityCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category Name")
    slug = models.SlugField(unique=True, db_index=True, help_text='URL-friendly identifier for the category.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Community Categories"

class CommunityPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='community_posts', verbose_name="User")
    category = models.ForeignKey(CommunityCategory, on_delete=models.CASCADE, related_name='posts', verbose_name="Category")
    title = models.CharField(max_length=50, verbose_name="Post Title")
    slug = models.SlugField(unique=True, db_index=True)
    timeline = models.CharField(max_length=100, verbose_name="Timeline")
    price = models.IntegerField(verbose_name="Price")
    skills = models.CharField(max_length=255, verbose_name="Skills Required")
    responsibilities = models.CharField(max_length=255, verbose_name="Responsibilities")
    description = models.TextField(verbose_name="Description")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Community Post"
        verbose_name_plural = "Community Posts"

@receiver(pre_save, sender=CommunityPost)
def pre_save_community_post(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

@receiver(pre_save, sender=CommunityCategory)
def pre_save_community_category(sender, instance, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)