from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'jewelry/pages/home.html')


def contact(request):
    return render(request, 'jewelry/pages/contact.html')


def login(request):
    return render(request, 'jewelry/pages/login.html')


def jewel(request):
    return render(request, 'jewelry/pages/jewel.html')
