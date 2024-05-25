from django.shortcuts import get_object_or_404, render
from django.views import View
from .models import Post, Category

# Blog listing view
def blog(request):
    posts = Post.objects.filter(is_published=True).order_by('-created_at')
    categories = Category.objects.all()
    context = {
        'posts': posts,
        'categories': categories
    }

    return render(request, 'blog.html', context)

# Single post detail view
class BlogSingle(View):
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        session_key = f'viewed_post_{post.id}'
        if not request.session.get(session_key, False):
            post.views_count += 1
            post.save(update_fields=['views_count'])
            request.session[session_key] = True
        return render(request, 'blog-single.html', {'post': post})