from django.views import View
from django.db.models import F
from django.db import transaction
from django.http import JsonResponse
from django.db.models import Avg, Count
from user_account.models import CustomUser, Review
from .models import CommunityCategory, CommunityPost
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

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
        user = get_object_or_404(CustomUser, username=post.user)
        reviews = Review.objects.filter(reviewed_user=user)
        # Calculate average rating
        avg_rating = reviews.aggregate(Avg('rating'))['rating__avg'] or 0
        # Calculate distribution of ratings
        rating_counts = reviews.values('rating').annotate(count=Count('rating')).order_by('rating')

        context = {
            'user_data': user,
            'post': post,
            'reviews': reviews,
            'avg_rating': avg_rating,
            'rating_counts': rating_counts,
        }

        return render(request, 'community-post.html', context)
    

@require_POST
def like_post(request, post_id):
    post = get_object_or_404(CommunityPost, id=post_id)
    with transaction.atomic():
        post.likes = F('likes') + 1
        post.save(update_fields=['likes'])
        post.refresh_from_db(fields=['likes'])
    return JsonResponse({'likes': post.likes, 'dislikes': post.dislikes})

@require_POST
def dislike_post(request, post_id):
    post = get_object_or_404(CommunityPost, id=post_id)
    with transaction.atomic():
        post.dislikes = F('dislikes') + 1
        post.save(update_fields=['dislikes'])
        post.refresh_from_db(fields=['dislikes'])
    return JsonResponse({'likes': post.likes, 'dislikes': post.dislikes})
    