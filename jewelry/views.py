from data import generator_contact, generator_jewel
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'jewelry/pages/home.html', context={
        'contacts': [generator_contact() for _ in range(25)],
    })


def contact(request):
    return render(request, 'jewelry/pages/contact.html', context={
        'contacts': [generator_contact() for _ in range(25)],
    })


def newcontact(request):
    return render(request, 'jewelry/pages/newcontact.html')


def updatecontact(request):
    return render(request, 'jewelry/pages/updatecontact.html')


def login(request):
    return render(request, 'jewelry/pages/login.html')


def jewel(request):
    return render(request, 'jewelry/pages/jewel.html', context={
        'jewelry': [generator_jewel() for _ in range(30)],
    })


def newjewel(request):
    return render(request, 'jewelry/pages/newjewel.html')


def updatejewel(request):
    return render(request, 'jewelry/pages/updatejewel.html')


def settingsjewel(request):
    return render(request, 'jewelry/pages/settingsjewel.html')
