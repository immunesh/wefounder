# Generated by Django 5.0.6 on 2024-06-18 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_review_contact_remove_review_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='post',
        ),
    ]