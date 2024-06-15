from django.views import View
from .models import CommunityCategory, CommunityPost
from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.
@login_required(login_url='signin')
def Community(request):
    communities = CommunityCategory.objects.all()
    CategoryName = request.GET.get('community',None)
    if CategoryName:
        category = CommunityCategory.objects.get(name=CategoryName)
        posts = CommunityPost.objects.filter(category=category)
    elif request.method == 'POST':
        data = request.POST.get('search_filter')
        posts = CommunityPost.objects.filter(title__icontains=data)
    else:
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