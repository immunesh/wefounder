from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
def home(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        company = request.POST['company']
        message = request.POST['message']
        data = Contact(name = name, email = email, phone = number, company = company, Message=message)
        messages.success(request,'Message was Successfully send !!!')
        return redirect('contact')
    else:
        return render(request,'contact.html')

def blog(request):
    return render(request,'blog.html')

def blog_single(request):
    return render(request,'blog-single.html')

def faqs(request):
    faq = Faq.objects.all()
    context = {
        'faq':faq,
    }
    return render(request,'faq.html', context)

def SignUpSteps(request):
    return render(request, 'sign-up-steps.html')