from django.views import View
from .models import CommunityCategory, CommunityPost
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@login_required(login_url='signin')
def Community(request):
    communities = CommunityCategory.objects.all()
    posts = CommunityPost.objects.all()

    context = {
        'communities': communities,
        'posts': posts
    }

    return render(request, 'community.html', context)

@method_decorator(login_required(login_url='signin'), name='dispatch')
class CommunitySingle(View):
    def get(self, request, slug):
        post = get_object_or_404(CommunityPost, slug=slug)
        return render(request, 'community-post.html', {'post': post})