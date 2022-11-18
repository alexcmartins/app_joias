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
    model_jewelry = models.ModelsJewelry.objects.all().order_by('-id')
    pearls = models.TypesPearls.objects.all().order_by('-id')
    if request.method == "GET":
        form = forms.IndicatorsForm(request.GET)
        form_cj = forms.CategoryJewelryForm(request.GET)
        form_mj = forms.ModelsJewelryForm(request.GET)
        form_pearls = forms.TypesPearlsForm(request.GET)
        return render(request, 'jewelry/pages/settings_jewel.html', context={
            'daily_indicators': daily_indicators,
            'category_jewelry': category_jewelry,
            'model_jewelry': model_jewelry,
            'pearls': pearls,
            'form': form,
            'form_cj': form_cj,
            'form_mj': form_mj,
            'form_pearls': form_pearls,
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


def update_indicators(request, id):
    indicators = models.Indicators.objects.get(id=id)
    form = forms.IndicatorsForm(request.POST or None, instance=indicators)
    if request.method == "POST":
        form = forms.IndicatorsForm(request.POST)
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


def update_models_settings(request, id):
    model_jewelry = models.ModelsJewelry.objects.get(id=id)
    form = forms.ModelsJewelryForm(
        request.POST or None, instance=model_jewelry)
    if request.method == "POST":
        form = forms.ModelsJewelryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jewelry:settings-jewel')

    return render(request, 'jewelry/partials/update_indicators.html',
                  context={
                      'model_jewelry': model_jewelry,
                      'form': form,
                  })


def delete_models_settings(request, id):
    model_jewelry = models.ModelsJewelry.objects.get(id=id)
    model_jewelry.delete()

    return redirect('jewelry:settings-jewel')


def update_category_settings(request, id):
    category_jewelry = models.CategoryJewelry.objects.get(id=id)
    form = forms.CategoryJewelryForm(
        request.POST or None, instance=category_jewelry)
    if request.method == "POST":
        form = forms.CategoryJewelryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jewelry:settings-jewel')

    return render(request, 'jewelry/partials/update_indicators.html',
                  context={
                      'category_jewelry': category_jewelry,
                      'form': form,
                  })


def delete_category_settings(request, id):
    category_jewelry = models.CategoryJewelry.objects.get(id=id)
    category_jewelry.delete()

    return redirect('jewelry:settings-jewel')


def update_pearls_settings(request, id):
    pearls = models.Pearls.objects.get(id=id)
    form = forms.TypesPearlsForm(request.POST or None, instance=pearls)
    if request.method == "POST":
        form = forms.TypesPearlsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jewelry:settings-jewel')

    return render(request, 'jewelry/partials/update_indicators.html',
                  context={
                      'pearls': pearls,
                      'form': form,
                  })


def delete_pearls_settings(request, id):
    pearls = models.Pearls.objects.get(id=id)
    pearls.delete()

    return redirect('jewelry:settings-jewel')


def update_stones_settings(request, id):
    stones = models.Stones.objects.get(id=id)
    form = forms.TypesStonesForm(request.POST or None, instance=stones)
    if request.method == "POST":
        form = forms.TypesStonesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jewelry:settings-jewel')

    return render(request, 'jewelry/partials/update_indicators.html',
                  context={
                      'stones': stones,
                      'form': form,
                  })


def delete_stones_settings(request, id):
    stones = models.Stones.objects.get(id=id)
    stones.delete()

    return redirect('jewelry:settings-jewel')


def teste(request):
    # condição caso o GET seja requisitado
    if request.method == "GET":
        """Aqui pegamos o campo selecionado para isso precisamos
        inserir um name="select" no proprio select"""
        select_itens = request.GET.get('select', '')
        # Aqui avaliamos se ele está nulo ou não
        if select_itens != '':
            # como é um teste eu fui printando o resultado
            print(select_itens)
            """ Aqui eu atribui a uma variavel a busca, usando filer e Q
            Como nesse meu model eu estou usando um forenKey precisei
            primeiro mencionar o model relacionado category, depois o campo
            no model, em seguida utilizei o icontains, mas dependendo do
            caso pode ser outro."""
            models_filters = models.ModelsJewelry.objects.filter(
                Q(category__name__icontains=select_itens),
            ).order_by('-category')
            # Aqui acompanhei mais uma vez o resultado
            print(models_filters)

            return render(request, 'jewelry/pages/add_teste.html', context={
                'select_itens': select_itens,
                'models_filters': models_filters,
            })
        else:
            models_1 = models.ModelsJewelry.objects.all().order_by('-id')
            print(models_1)
            return render(request, 'jewelry/pages/add_teste.html', context={
                'models_1': models_1,
            })
