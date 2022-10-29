from data import generator_contact, generator_jewel
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'jewelry/pages/home.html', context={
        'contacts': [generator_contact() for _ in range(25)],
    })


def contact(request, id):
    return render(request, 'jewelry/pages/contact.html', context={
        'contact': generator_contact(),
    })


def newcontact(request):
    return render(request, 'jewelry/pages/newcontact.html')


def updatecontact(request):
    return render(request, 'jewelry/pages/updatecontact.html')


def login(request):
    return render(request, 'jewelry/pages/login.html')


def jewelry(request):
    return render(request, 'jewelry/pages/jewelry.html', context={
        'jewelry': [generator_jewel() for _ in range(30)],
    })


def jewel(request, id):
    return render(request, 'jewelry/pages/jewel.html', context={
        'jewel': generator_jewel(),
    })


def newjewel(request):
    return render(request, 'jewelry/pages/newjewel.html')


def updatejewel(request):
    return render(request, 'jewelry/pages/updatejewel.html')


def settingsjewel(request):
    return render(request, 'jewelry/pages/settingsjewel.html')
