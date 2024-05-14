from django.shortcuts import render

def home(request):
    return render(request,'index.html')

def signUp(request):
    return render(request,'sign-up.html')

def signIn(request):
    return render(request,'sign-in.html')

def userProfile(request):
    return render(request,'account-detail.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def blog_single(request):
    return render(request,'blog-single.html')

def faqs(request):
    return render(request,'faq.html')