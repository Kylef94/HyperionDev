from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request, "index.html")

def tindog(request):
    return render(request, "tindog.html")

def personal(request):
    return render(request, "personal-site.html")