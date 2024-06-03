from django.shortcuts import render

# Create your views here.

def Community(request):
    return render(request, 'community.html')