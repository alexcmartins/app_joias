from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

from data import generator_jewel

from . import forms, models


# Home - List all contacts and search
def home(request):
    if request.method == "GET":
        search_term = request.GET.get('search', '')
        if search_term != '':
            print(search_term)
            contacts_filters = models.Contacts.objects.filter(
                Q(first_name__icontains=search_term) |
                Q(last_name__icontains=search_term) |
                Q(notes__icontains=search_term),
            ).order_by('-id')
            print(contacts_filters)

            return render(request, 'jewelry/pages/home.html', context={
                'first_name': f'Search for"{search_term}" |',
                'search_term': search_term,
                'contacts_filters': contacts_filters,
            })
        else:
            contacts = models.Contacts.objects.all().order_by('-id')
            return render(request, 'jewelry/pages/home.html', context={
                'contacts': contacts,
            })


# View contact
def contact(request, id):
    contact = models.Contacts.objects.filter(id=id).order_by('-id').first()
    return render(request, 'jewelry/pages/contact.html', context={
        'contact': contact,
    })


# Create new contact
def new_contact(request):
    submitted = False
    if request.method == "POST":
        form = forms.ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            contact.save()
            return HttpResponseRedirect('/contacts/new?submitted=True')
    else:
        form = forms.ContactForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'jewelry/pages/new_contact.html', context={
        'form': form,
        'submitted': submitted,
    })


# Update contact
def update_contact(request, id):
    contact = models.Contacts.objects.get(id=id)
    if request.method == "GET":
        form = forms.ContactForm(
            request.GET or None, instance=contact)

        return render(request, 'jewelry/pages/update_contact.html', context={
            'contact': contact,
            'form': form,
        })

    else:
        form = forms.ContactForm(
            request.POST, request.FILES or None, instance=contact)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')

        return render(request, 'jewelry/pages/update_contact.html', context={
            'contact': contact,
            'form': form,
        })


# Delete Contact
def delete_contact(request, id):
    contact = models.Contacts.objects.get(id=id)
    contact.delete()

    return redirect('/')


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
    daily_indicators = models.Indicators.objects.all().order_by('-id')
    category_jewelry = models.CategoryJewelry.objects.all().order_by('-id')
    if request.method == "GET":
        form = forms.IndicatorsForm(request.GET)
        form_cj = forms.CategoryJewelryForm(request.GET)
        return render(request, 'jewelry/pages/settings_jewel.html', context={
            'daily_indicators': daily_indicators,
            'category_jewelry': category_jewelry,
            'form': form,
            'form_cj': form_cj,
        })

    else:
        form = forms.IndicatorsForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('settings')

        return render(request, 'jewelry/pages/settings_jewel.html', context={
            'daily_indicators': daily_indicators,
            'form': form,
        })


"""
def update_indicators(request, id):
    indicators = models.Indicators.objects.get(id=id)
    if request.method == "GET":
        form = forms.IndicatorsForm(
            request.GET or None, instance=indicators)

        return render(request, 'jewelry/partials/update_indicators.html',
                      context={
                          'indicators': indicators,
                          'form': form,
                      })

    else:
        form = forms.IndicatorsForm(
            request.POST, request.FILES or None, instance=indicators)
        if form.is_valid():
            form.save()
            return redirect('jewelry:settings-jewel')

        return render(request, 'jewelry/partials/update_indicators.html',
                      context={
                          'indicators': indicators,
                          'form': form,
                      })
"""


def update_indicators(request, id):
    indicators = models.Indicators.objects.get(id=id)
    form = forms.IndicatorsForm(request.POST or None, instance=indicators)
    if request.method == "POST":
        indicators = models.Indicators.objects.get(id=id)
        form = forms.IndicatorsForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('jewelry:settings-jewel')

    return render(request, 'jewelry/partials/update_indicators.html',
                  context={
                      'indicators': indicators,
                      'form': form,
                  })


def delete_indicators(request, id):
    indicators = models.Indicators.objects.get(id=id)
    indicators.delete()

    return redirect('jewelry:settings-jewel')
