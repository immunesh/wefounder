from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'slug', 'content', 'excerpt', 'category', 'tags',
            'featured_image', 'featured_title', 'featured_alt_text',
            'is_published', 'meta_title', 'meta_description', 'meta_keywords'
        ]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'content']
