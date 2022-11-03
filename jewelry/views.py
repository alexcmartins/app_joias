from django.db.models import Q
from django.shortcuts import render

from data import generator_jewel

from .models import Contacts


# Create your views here.
def home(request):
    search_term = request.GET.get('search', '')
    print(search_term)
    contacts_filters = Contacts.objects.filter(
        Q(first_name__icontains=search_term) |
        Q(last_name__icontains=search_term),
    ).order_by('-id')
    print(contacts_filters)
    contacts = Contacts.objects.all().order_by('-id')

    return render(request, 'jewelry/pages/home.html', context={
        # 'first_name': f'Search for"{search_term}" |',
        'search_term': search_term,
        'contacts': contacts,
        'contacts_filters': contacts_filters,
    })


def contact(request, id):
    contact = Contacts.objects.filter(id=id).order_by('-id').first()
    return render(request, 'jewelry/pages/contact.html', context={
        'contact': contact,
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
