from urllib import request

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def portfolio_details(request):
    return render(request, 'portfolio-details.html')

def service_details(request):
    return render(request, 'service-details.html')

def about(request):
    return render(request, 'About.html')

def contact(request):
    return render(request, 'contact .html')

def team(request):
    return render(request, 'team.html')
def start(request):
    return render(request, 'Start.html')
