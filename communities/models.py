from django.db import models
from django.utils.text import slugify
from django.dispatch import receiver
from django.db.models.signals import pre_save
from user_account.models import CustomUser
from django.conf import settings


class CommunityCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Category Name")
    slug = models.SlugField(unique=True, db_index=True, help_text='URL-friendly identifier for the category.')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Community Categories"
        
# class Sector(models.Model):
#     name = models.CharField(max_length=100, unique=True, verbose_name="sector")

#     def __str__(self):
#         return self.name
    
# class SubSector(models.Model):
#     name = models.CharField(max_length=100, unique=True, verbose_name="subsector")

#     def __str__(self):
#         return self.name

class CommunityPost(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='community_posts', verbose_name="User")
    category = models.ForeignKey(CommunityCategory, on_delete=models.CASCADE, related_name='posts', verbose_name="Category")
    title = models.CharField(max_length=50, verbose_name="Post Title")
    slug = models.SlugField(unique=True, db_index=True)
    sector = models.CharField(max_length=100,default="default_sector")
    sub_sector = models.CharField(max_length=100,default="default_sub_sector")
    # sector = models.ForeignKey(Sector, on_delete=models.CASCADE, verbose_name="sector")
    # sub_sector = models.ForeignKey(SubSector, on_delete=models.CASCADE, verbose_name="subsector")
    # skills = models.CharField(max_length=255, verbose_name="Skills Required")
    # responsibilities = models.CharField(max_length=255, verbose_name="Responsibilities")
    description = models.TextField(verbose_name="Description",default='default_description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)

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