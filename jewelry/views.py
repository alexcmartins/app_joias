from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render

from data import generator_jewel

from .forms import NewContactForm
from .models import Contacts


# Home - List all contacts and search
def home(request):
    if request.method == "GET":
        search_term = request.GET.get('search', '')
        if search_term != '':
            print(search_term)
            contacts_filters = Contacts.objects.filter(
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term),
            ).order_by('-id')
            print(contacts_filters)

            return render(request, 'jewelry/pages/home.html', context={
                'first_name': f'Search for"{search_term}" |',
                'search_term': search_term,
                'contacts_filters': contacts_filters,
            })
        else:
            contacts = Contacts.objects.all().order_by('-id')
            return render(request, 'jewelry/pages/home.html', context={
                'contacts': contacts,
            })


# View contact
def contact(request, id):
    contact = Contacts.objects.filter(id=id).order_by('-id').first()
    return render(request, 'jewelry/pages/contact.html', context={
        'contact': contact,
    })


# Create new contact
def new_contact(request):
    submitted = False
    if request.method == "POST":
        form = NewContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            contact.save()
            return HttpResponseRedirect('/contacts/new?submitted=True')
    else:
        form = NewContactForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'jewelry/pages/new_contact.html', context={
        'form': form,
        'submitted': submitted,
    })


# Update contact
def update_contact(request, id):
    contact = Contacts.objects.filter(id=id).order_by('-id').first()
    return render(request, 'jewelry/pages/update_contact.html', context={
        'contact': contact,
    })


# Login
def login(request):
    return render(request, 'jewelry/pages/login.html')


# List all jewelry
def jewelry(request):
    return render(request, 'jewelry/pages/jewelry.html', context={
        'jewelry': [generator_jewel() for _ in range(30)],
    })


# View jewel
def jewel(request, id):
    return render(request, 'jewelry/pages/jewel.html', context={
        'jewel': generator_jewel(),
    })


# Create new jewel
def new_jewel(request):
    return render(request, 'jewelry/pages/new_jewel.html')


# Update jewel
def update_jewel(request):
    return render(request, 'jewelry/pages/update_jewel.html')


# Settings jewelry
def settings_jewel(request):
    return render(request, 'jewelry/pages/settings_jewel.html')
