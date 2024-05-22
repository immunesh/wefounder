from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from .models import CustomUser

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

        # Check if email already exists
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already taken.")
            return render(request, 'sign-up.html')

        # Create the new user
        user = CustomUser(
            email=email,
            full_name =full_name,
            username=username,
            password=make_password(password)
        )
        # user.save()

        return render(request, 'sign-up-steps.html')

        # # Automatically log in the user after successful sign up
        # login(request, user)
        # messages.success(request, "Account created successfully.")
        # return redirect('viewProfile', username=user.username)

    return render(request, 'sign-up.html')

def signUpSteps(request):
    if request.method == "POST":
        location = request.POST.get('location')
        looking_for = request.POST.get('looking_for')
        i_can = request.POST.get('i_can')
        description = request.POST.get('description')
        profession = request.POST.get('profession')
        experience = request.POST.get('experience')
        skills_and_expertise = request.POST.get('skills_and_expertise')

        user = CustomUser(
            location=location,
            looking_for =looking_for,
            i_can=i_can,
            description=description,
            profession=profession,
            experience=experience,
            skills_and_expertise=skills_and_expertise
        )
        user.save()


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
def logOut(request):
    logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def deleteAccount(request):
    if request.method == "POST":
        user = request.user
        user.delete()
        logout(request)
        messages.success(request, "Your account has been deleted.")
        return redirect('signin')

    return render(request, 'user-account-dashboard/account-delete.html')

@login_required(login_url='signin')
def userProfile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'user-account-dashboard/account-detail.html', {'user': user})

@login_required(login_url='signin')
def accountSecurity(request):
    return render(request, 'user-account-dashboard/account-security.html')

@login_required(login_url='signin')
def accountNotification(request):
    return render(request, 'user-account-dashboard/account-notification.html')

@login_required(login_url='signin')
def accountProjects(request):
    return render(request, 'user-account-dashboard/account-projects.html')

@login_required(login_url='signin')
def paymentDetails(request):
    return render(request, 'user-account-dashboard/account-payment-details.html')

@login_required(login_url='signin')
def order(request):
    return render(request, 'user-account-dashboard/account-order.html')

@login_required(login_url='signin')
def wishlist(request):
    return render(request, 'user-account-dashboard/account-wishlist.html')