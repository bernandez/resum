from django.shortcuts import render
from .models import Resume


# Create your views here.


def home(request):
    return render(request, 'resum/home.html')


def about(request):
    resume = Resume.objects.get(pk=1)
    return render(request, 'resum/about.html', {"resume": resume})


def contact(request):
    return render(request, 'resum/contact.html')


def portfolio(request):
    return render(request, 'resum/portfolio.html')


def blog(request):
    return render(request, 'resum/blog.html')