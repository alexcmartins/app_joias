
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):
    return render(request, 'login.html')


def jewel(request):
    return render(request, 'jewel.html')
