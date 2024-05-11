from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def signUp(request):
    return render(request,'sign-up.html')

def signIn(request):
    return render(request,'sign-in.html')

def userProfile(request):
    return render(request,'account-detail.html')