from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import CommunityCategory, CommunityPost

# Create your views here.
@login_required(login_url='signin')
def Community(request):
    try:
        communities = CommunityCategory.objects.all()
        posts = CommunityPost.objects.all()
    except communities.DoesNotExist:
        communities = None
        posts = None

    context = {
        'communities': communities,
        'posts': posts
    }

    return render(request, 'community.html', context)

@login_required(login_url='signin')
def communitySingle(request):
    return render(request, 'community-post.html')