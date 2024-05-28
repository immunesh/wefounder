from .models import CustomUser
from django.db import transaction
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout

# Create your views here.
@transaction.atomic
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

        request.session['user_id'] = user.id

        return redirect('signUpSteps')

    return render(request, 'sign-up.html')

@transaction.atomic
def signUpSteps(request):
    if request.method == "POST":
        role = request.POST.get('role')
        company = request.POST.get('company')
        city = request.POSt.get('city')
        zip_code = request.POST.get('zip-code')
        looking_for = request.POST.get('looking_for')
        i_can = request.POST.get('i_can')
        skills_and_expertise = request.POST.get('skills_expertise')

        user_id = request.session.get('user_id')
        if not user_id:
            print("No")
            messages.error(request, "Session expired. Please sign up again.")
            return redirect('signUp')

        try:
            user = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            messages.error(request, "User not found. Please sign up again.")
            return redirect('signUp')

        user.role = role
        user.company = company
        user.city = city
        user.zip_code = zip_code
        user.looking_for = looking_for
        user.i_can = i_can
        user.skills_expertise = skills_and_expertise
        user.save()

        login(request, user)
        messages.success(request, "Account created successfully.")
        return redirect('viewProfile', username=user.username)
    return render(request, 'sign-up-steps.html')

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

def profile(request):
    return render(request, 'user-account-dashboard/user-profile.html')

@login_required(login_url='signin')
def wishlist(request):
    return render(request, 'user-account-dashboard/account-wishlist.html')