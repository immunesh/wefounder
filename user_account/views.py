from .models import CustomUser
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from communities.models import CommunityCategory, CommunityPost

# Create your views here.
def signUp(request):
    if request.method == "POST":
        email = request.POST.get('gmail_id')
        full_name = request.POST.get('full_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if not username or not email or not password or not confirm_password or not full_name:
            messages.error(request, "All fields are required.")
            return render(request, 'sign-up.html')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'sign-up.html')

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return render(request, 'sign-up.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already taken.")
            return render(request, 'sign-up.html')

        user = CustomUser(
            email=email,
            full_name=full_name,
            username=username,
            password=make_password(password)
        )
        user.save()

        return redirect('signUpSteps', user_id=user.id)

    return render(request, 'sign-up.html')

def signUpSteps(request, user_id):
    try:
        user = CustomUser.objects.get(id=user_id)
    except CustomUser.DoesNotExist:
        messages.error(request, "User does not exist.")
        return redirect('signUp')

    if request.method == "POST":
        role = request.POST.get('role')
        company = request.POST.get('company')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip_code')
        looking_for = request.POST.getlist('looking_for')
        i_can = request.POST.getlist('i_can')
        skills_expertise = request.POST.get('skills_expertise')

        # Validate that all fields are provided
        if not all([role, company, city, zip_code, looking_for, i_can, skills_expertise]):
            messages.error(request, "All fields are required.")
            return render(request, 'sign-up-steps.html', {'user': user})

        # Update the user with additional information
        user.role = role
        user.company = company
        user.city = city
        user.zip_code = zip_code
        user.looking_for = looking_for
        user.i_can = i_can
        user.skills_expertise = skills_expertise
        user.save()

        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect('viewProfile', username=user.username)
    
    context = {
        'user': user,
        'looking_for_options': [
            {'id': 'advisor', 'value': 'Advisor', 'label': 'Advisor'},
            {'id': 'job', 'value': 'Job', 'label': 'Job'},
            {'id': 'mentor', 'value': 'Mentor', 'label': 'Mentor'},
            {'id': 'investor', 'value': 'Investor', 'label': 'Investor'},
            {'id': 'collaborator', 'value': 'Collaborator', 'label': 'Collaborator'},
            {'id': 'warm_intro', 'value': 'Warm_intro', 'label': 'Warm intro'},
            {'id': 'feedback', 'value': 'Feedback', 'label': 'Feedback'},
            {'id': 'cofounder', 'value': 'Co-founder', 'label': 'Co-founder'},
            {'id': 'freelancer_consultant', 'value': 'Freelancer_consultant', 'label': 'Freelancer/consultant'},
            {'id': 'volunteers', 'value': 'Volunteers', 'label': 'Volunteers'},
            {'id': 'internship', 'value': 'Internship', 'label': 'Internship'},
            {'id': 'startup_to_join', 'value': 'Startup_to_join', 'label': 'Startup to join'},
            {'id': 'press_publicity', 'value': 'Press_Publicity', 'label': 'Press/Publicity'},
            {'id': 'users_customers', 'value': 'Users_customers', 'label': 'Users/customers'},
            {'id': 'inspiration', 'value': 'Inspiration', 'label': 'Inspiration'},
            {'id': 'smart_people', 'value': 'Smart_people', 'label': 'Smart people'},
            {'id': 'new_perspectives', 'value': 'New_perspectives', 'label': 'New perspectives'},
            {'id': 'next_unicorn', 'value': 'Next_unicorn', 'label': 'Next unicorn'},
            {'id': 'next_challenge', 'value': 'Next_challenge', 'label': 'Next challenge'},
            {'id': 'moonshots', 'value': 'Moonshots', 'label': 'Moonshots'},
            {'id': 'an_active_network', 'value': 'An_active_network', 'label': 'An active network'},
            {'id': 'startup_ideas', 'value': 'Startup_ideas', 'label': 'Startup ideas'},
            {'id': 'grow_my_startup', 'value': 'Grow_my_startup', 'label': 'Grow my startup'},
            {'id': 'learn_something_new', 'value': 'Learn_something_new', 'label': 'Learn something new'},
            {'id': 'upskill', 'value': 'Upskill', 'label': 'Upskill'},
        ],
        'i_can_options': [
            {'id': 'invest', 'value': 'Invest', 'label': 'Invest'},
            {'id': 'collaborat', 'value': 'Collaborator', 'label': 'Collaborator'},
            {'id': 'introduce', 'value': 'Introduce you', 'label': 'Introduce you'},
            {'id': 'give_feedback', 'value': 'Give Feedback', 'label': 'Give Feedback'},
            {'id': 'teach', 'value': 'Teach', 'label': 'Teach'},
            {'id': 'freelancer_consult', 'value': 'Freelancer Consult', 'label': 'Freelancer/Consult'},
            {'id': 'volunteer', 'value': 'Volunteer', 'label': 'Volunteer'},
            {'id': 'cofound', 'value': 'Co-found', 'label': 'Co-found'},
            {'id': 'sell', 'value': 'Sell', 'label': 'Sell'},
            {'id': 'promote_product', 'value': 'Promote Product', 'label': 'Promote product'},
            {'id': 'speak_events', 'value': 'Speak at events', 'label': 'Speak at events'},
            {'id': 'create_content', 'value': 'Create Content', 'label': 'Create Content'},
            {'id': 'growth_hack', 'value': 'Growth Hack', 'label': 'Growth Hack'},
            {'id': 'ideate', 'value': 'Ideate', 'label': 'Ideate'},
        ],
    }

    return render(request, 'sign-up-steps.html', context)

def signIn(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not username or not password:
            messages.error(request, "All fields are required.")
            return render(request, 'sign-in.html')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in.")
            return redirect('viewProfile', username=user.username)
        else:
            messages.error(request, "Invalid username or password.")
            return render(request, 'sign-in.html')

    return render(request, 'sign-in.html')

@login_required(login_url='signin')
def updateProfile(request, username):
    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        messages.error(request, "User does not exist.")
        return redirect('signUp')
    
    if request.method == "POST":
        email = request.POST.get('email')
        current_pass = request.POST.get('current_pass')
        new_password = request.POST.get('new_password')
        cf_new_password = request.POST.get('cf_new_password')

        # Update email if provided
        if email:
            user.email = email
            user.save()
            print("Email updated successfully.")
            messages.success(request, "Email updated successfully.")
            return redirect('viewProfile', user.username)

        # Update password if new passwords match and current password is correct
        if new_password and cf_new_password:
            if new_password == cf_new_password:
                if authenticate(username=user.username, password=current_pass):
                    user.set_password(new_password)
                    user.save()
                    print("Password updated successfully.")
                    messages.success(request, "Password updated successfully.")
                    login(request, user)
                    return redirect('viewProfile', user.username)
                else:
                    print("Current password is incorrect.")
                    messages.error(request, "Current password is incorrect.")
                    return redirect('viewProfile', user.username)
            else:
                print("New passwords do not match.")
                messages.error(request, "New passwords do not match.")
                return redirect('viewProfile', user.username)
    
    return redirect('viewProfile', user.username)

@login_required(login_url='signin')
def logOut(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def userProfile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    context = {
        'user': user,
        'looking_for_options': [
            {'id': 'advisor', 'value': 'Advisor', 'label': 'Advisor'},
            {'id': 'job', 'value': 'Job', 'label': 'Job'},
            {'id': 'mentor', 'value': 'Mentor', 'label': 'Mentor'},
            {'id': 'investor', 'value': 'Investor', 'label': 'Investor'},
            {'id': 'collaborator', 'value': 'Collaborator', 'label': 'Collaborator'},
            {'id': 'warm_intro', 'value': 'Warm_intro', 'label': 'Warm intro'},
            {'id': 'feedback', 'value': 'Feedback', 'label': 'Feedback'},
            {'id': 'cofounder', 'value': 'Co-founder', 'label': 'Co-founder'},
            {'id': 'freelancer_consultant', 'value': 'Freelancer_consultant', 'label': 'Freelancer/consultant'},
            {'id': 'volunteers', 'value': 'Volunteers', 'label': 'Volunteers'},
            {'id': 'internship', 'value': 'Internship', 'label': 'Internship'},
            {'id': 'startup_to_join', 'value': 'Startup_to_join', 'label': 'Startup to join'},
            {'id': 'press_publicity', 'value': 'Press_Publicity', 'label': 'Press/Publicity'},
            {'id': 'users_customers', 'value': 'Users_customers', 'label': 'Users/customers'},
            {'id': 'inspiration', 'value': 'Inspiration', 'label': 'Inspiration'},
            {'id': 'smart_people', 'value': 'Smart_people', 'label': 'Smart people'},
            {'id': 'new_perspectives', 'value': 'New_perspectives', 'label': 'New perspectives'},
            {'id': 'next_unicorn', 'value': 'Next_unicorn', 'label': 'Next unicorn'},
            {'id': 'next_challenge', 'value': 'Next_challenge', 'label': 'Next challenge'},
            {'id': 'moonshots', 'value': 'Moonshots', 'label': 'Moonshots'},
            {'id': 'an_active_network', 'value': 'An_active_network', 'label': 'An active network'},
            {'id': 'startup_ideas', 'value': 'Startup_ideas', 'label': 'Startup ideas'},
            {'id': 'grow_my_startup', 'value': 'Grow_my_startup', 'label': 'Grow my startup'},
            {'id': 'learn_something_new', 'value': 'Learn_something_new', 'label': 'Learn something new'},
            {'id': 'upskill', 'value': 'Upskill', 'label': 'Upskill'},
        ],
        'i_can_options': [
            {'id': 'invest', 'value': 'Invest', 'label': 'Invest'},
            {'id': 'collaborat', 'value': 'Collaborator', 'label': 'Collaborator'},
            {'id': 'introduce', 'value': 'Introduce you', 'label': 'Introduce you'},
            {'id': 'give_feedback', 'value': 'Give Feedback', 'label': 'Give Feedback'},
            {'id': 'teach', 'value': 'Teach', 'label': 'Teach'},
            {'id': 'freelancer_consult', 'value': 'Freelancer Consult', 'label': 'Freelancer/Consult'},
            {'id': 'volunteer', 'value': 'Volunteer', 'label': 'Volunteer'},
            {'id': 'cofound', 'value': 'Co-found', 'label': 'Co-found'},
            {'id': 'sell', 'value': 'Sell', 'label': 'Sell'},
            {'id': 'promote_product', 'value': 'Promote Product', 'label': 'Promote product'},
            {'id': 'speak_events', 'value': 'Speak at events', 'label': 'Speak at events'},
            {'id': 'create_content', 'value': 'Create Content', 'label': 'Create Content'},
            {'id': 'growth_hack', 'value': 'Growth Hack', 'label': 'Growth Hack'},
            {'id': 'ideate', 'value': 'Ideate', 'label': 'Ideate'},
        ],
    }
    return render(request, 'user-account-dashboard/account-detail.html', context)

@login_required(login_url='signin')
def accountNotification(request):
    return render(request, 'user-account-dashboard/account-notification.html')

@login_required(login_url='signin')
def accountProjects(request):
    
    if request.method == 'POST':
        category_id = request.POST.get('category')
        title = request.POST.get('title')
        timeline = request.POST.get('timeline')
        price = request.POST.get('price')
        skills = request.POST.get('skills')
        responsibilities = request.POST.get('responsibilities')
        description = request.POST.get('description')

        user = request.user

        if not price:
            price = 0

        try:
            category = CommunityCategory.objects.get(id=category_id)
            data = CommunityPost(
                user=user,
                category=category,
                title=title,
                timeline=timeline,
                price=price,
                skills=skills,
                responsibilities=responsibilities,
                description=description,
            )
            data.save()
            messages.success(request, 'Successfully added new Project!')
        except CommunityCategory.DoesNotExist:
            messages.error(request, 'Category does not exist!')

        return redirect('/account-projects/')

    communities = CommunityCategory.objects.all()
    projects = CommunityPost.objects.filter(user=request.user)

    context = {
        'communities': communities,
        'projects': projects,
    }

    return render(request, 'user-account-dashboard/account-projects.html', context)

@login_required(login_url='signin')
def accountProject_update(request, id=None):
    post = get_object_or_404(CommunityPost, id=id)
    
    if request.method == 'POST':
        post.category_id = request.POST.get('category')
        post.title = request.POST.get('title')
        post.timeline = request.POST.get('timeline')
        post.price = request.POST.get('price')
        post.skills = request.POST.get('skills')
        post.responsibilities = request.POST.get('responsibilities')
        post.description = request.POST.get('description')
        
        post.save()
        messages.success(request, "Post updated successfully.")
        return redirect('account_projects')
    
    elif request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = {
            'category': post.category_id,
            'title': post.title,
            'timeline': post.timeline,
            'price': post.price,
            'skills': post.skills,
            'responsibilities': post.responsibilities,
            'description': post.description,
        }
        return JsonResponse(data)
    
    context = {
        'post': post,
    }
    
    return render(request, 'user-account-dashboard/account-projects.html', context)

@login_required(login_url='signin')
def ProjectDelete(request, id = None):
    delete_project = CommunityPost.objects.get(id = id)
    delete_project.delete()
    messages.success(request, "Post deleted successfully.")
    return redirect('account_projects')

def profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    posts= CommunityPost.objects.filter(user=user)
    context ={
        'user_data': user,
        'posts': posts
    }
    return render(request, 'user-account-dashboard/user-profile.html', context)

@login_required(login_url='signin')
def Messages(request):
    return render(request, 'user-account-dashboard/account-wishlist.html')