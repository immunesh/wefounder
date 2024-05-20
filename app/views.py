from django.shortcuts import render

def home(request):
    return render(request,'index.html')

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

def SignUpSteps(request):
    return render(request, 'sign-up-steps.html')