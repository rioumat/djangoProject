from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'pages/index.html')

def about(request):
    logger.info("about page")
    return render(request, 'pages/about.html')
