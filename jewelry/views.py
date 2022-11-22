from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic.edit import UpdateView

from data import generator_jewel

from .forms import (CategoryJewelryForm, ContactForm, IndicatorsForm,
                    ModelsJewelryForm, TypesMetalsForm, TypesPearlsForm,
                    TypesStonesForm)
from .models import (CategoryJewelry, Contacts, Indicators, ModelsJewelry,
                     TypesMetals, TypesPearls, TypesStones)


# Home - List all contacts and search
def home(request):
    if request.method == "GET":
        search_term = request.GET.get('search', '')
        if search_term != '':
            print(search_term)
            contacts_filters = Contacts.objects.filter(
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
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            contact = form.save()
            contact.save()
            return HttpResponseRedirect('/contacts/new?submitted=True')
    else:
        form = ContactForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'jewelry/pages/new_contact.html', context={
        'form': form,
        'submitted': submitted,
    })


# Update contact
def update_contact(request, id):
    contact = Contacts.objects.get(id=id)
    if request.method == "GET":
        form = ContactForm(
            request.GET or None, instance=contact)

        return render(request, 'jewelry/pages/update_contact.html', context={
            'contact': contact,
            'form': form,
        })

    else:
        form = ContactForm(
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
    contact = Contacts.objects.get(id=id)
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
    daily_indicators = Indicators.objects.all().order_by('-id')
    category_jewelry = CategoryJewelry.objects.all().order_by('-id')
    model_jewelry = ModelsJewelry.objects.all().order_by('-id')
    pearls = TypesPearls.objects.all().order_by('-id')
    stones = TypesStones.objects.all().order_by('-id')
    metals = TypesMetals.objects.all().order_by('-id')

    return render(request, 'jewelry/pages/settings_jewel.html', context={
        'daily_indicators': daily_indicators,
        'category_jewelry': category_jewelry,
        'model_jewelry': model_jewelry,
        'pearls': pearls,
        'stones': stones,
        'metals': metals,
    })


def new_indicators(request):
    if request.method == "POST":
        form = IndicatorsForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/jewelry/settings')

    else:
        form = IndicatorsForm

        return render(request, 'jewelry/pages/new_settings.html', context={
            'form': form,
        })


def update_indicators(request, id):
    indicators = Indicators.objects.get(id=id)
    if request.method == "GET":
        form = IndicatorsForm(
            request.GET or None, instance=indicators)

        return render(request, 'jewelry/pages/update_settings.html', context={
            'indicators': indicators,
            'form': form,
        })

    else:
        form = IndicatorsForm(request.POST)
        if form.is_valid():
            up_indicators = form.save()
            up_indicators.save()
            return HttpResponseRedirect('/jewelry/settings')

    return render(request, 'jewelry/pages/update_settings.html', context={
        'indicators': indicators,
        'form': form,
    })


def delete_indicators(request, id):
    indicators = Indicators.objects.get(id=id)
    indicators.delete()

    return redirect('jewelry:settings-jewel')


def new_models_settings(request):
    if request.method == "POST":
        form = ModelsJewelryForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/jewelry/settings')
    else:
        form = ModelsJewelryForm

    return render(request, 'jewelry/pages/new_settings.html', context={
        'form': form,
    })


def update_models_settings(request, id):
    model_jewelry = ModelsJewelry.objects.get(id=id)
    form = ModelsJewelryForm(
        request.POST or None, instance=model_jewelry)
    if request.method == "POST":
        form = ModelsJewelryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jewelry:settings-jewel')

    return render(request, 'jewelry/pages/update_settings.html',
                  context={
                      'model_jewelry': model_jewelry,
                      'form': form,
                  })


def delete_models_settings(request, id):
    model_jewelry = ModelsJewelry.objects.get(id=id)
    model_jewelry.delete()

    return redirect('jewelry:settings-jewel')


def new_category_settings(request):
    if request.method == "POST":
        form = CategoryJewelryForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/jewelry/settings')
    else:
        form = CategoryJewelryForm

    return render(request, 'jewelry/pages/new_settings.html', context={
        'form': form,
    })


def update_category_settings(request, id):
    category_jewelry = CategoryJewelry.objects.get(id=id)
    form = CategoryJewelryForm(
        request.POST or None, instance=category_jewelry)
    if request.method == "POST":
        form = CategoryJewelryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jewelry:settings-jewel')

    return render(request, 'jewelry/pages/update_settings.html',
                  context={
                      'category_jewelry': category_jewelry,
                      'form': form,
                  })


def delete_category_settings(request, id):
    category_jewelry = CategoryJewelry.objects.get(id=id)
    category_jewelry.delete()

    return redirect('jewelry:settings-jewel')


def new_pearls_settings(request):
    if request.method == "POST":
        form = TypesPearlsForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/jewelry/settings')
    else:
        form = TypesPearlsForm

    return render(request, 'jewelry/pages/new_settings.html', context={
        'form': form,
    })


def update_pearls_settings(request, id):
    pearls = TypesPearls.objects.get(id=id)
    form = TypesPearlsForm(request.POST or None, instance=pearls)
    if request.method == "POST":
        form = TypesPearlsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jewelry:settings-jewel')

    return render(request, 'jewelry/pages/update_settings.html',
                  context={
                      'pearls': pearls,
                      'form': form,
                  })


def delete_pearls_settings(request, id):
    pearls = TypesPearls.objects.get(id=id)
    pearls.delete()

    return redirect('jewelry:settings-jewel')


def new_stones_settings(request):
    if request.method == "POST":
        form = TypesStonesForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/jewelry/settings')
    else:
        form = TypesStonesForm

    return render(request, 'jewelry/pages/new_settings.html', context={
        'form': form,
    })


def update_stones_settings(request, id):
    stones = TypesStones.objects.get(id=id)
    form = TypesStonesForm(request.POST or None, instance=stones)
    if request.method == "POST":
        form = TypesStonesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jewelry:settings-jewel')

    return render(request, 'jewelry/pages/update_settings.html',
                  context={
                      'stones': stones,
                      'form': form,
                  })


def delete_stones_settings(request, id):
    stones = TypesStones.objects.get(id=id)
    stones.delete()

    return redirect('jewelry:settings-jewel')


def new_metals_settings(request):
    if request.method == "POST":
        form = TypesMetalsForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/jewelry/settings')
    else:
        form = TypesMetalsForm

    return render(request, 'jewelry/pages/new_settings.html', context={
        'form': form,
    })


class MetalsUpdateView(UpdateView):
    template_name = "update_settings.html"
    form_class = TypesMetalsForm
    context_object_name = "metals"
    success_url = "/jewelry/settings"

    def get_object(self):
        id = self.kwargs.get(self.pk_url_kwarg)
        metals = TypesMetals.objects.filter(id=id).first()
        return metals


"""
def update_metals_settings(request, id):
    metals = models.TypesMetals.objects.get(id=id)
    form = forms.TypesMetalsForm(request.POST or None, instance=metals)
    if request.method == "POST":
        form = forms.TypesMetalsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jewelry:settings-jewel')

    return render(request, 'jewelry/pages/update_settings.html',
                  context={
                      'metals': metals,
                      'form': form,
                  })
"""


def delete_metals_settings(request, id):
    metals = TypesMetals.objects.get(id=id)
    metals.delete()

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
            models_filters = ModelsJewelry.objects.filter(
                Q(category__name__icontains=select_itens),
            ).order_by('-category')
            # Aqui acompanhei mais uma vez o resultado
            print(models_filters)

            return render(request, 'jewelry/pages/add_teste.html', context={
                'select_itens': select_itens,
                'models_filters': models_filters,
            })
        else:
            models_1 = ModelsJewelry.objects.all().order_by('-id')
            print(models_1)
            return render(request, 'jewelry/pages/add_teste.html', context={
                'models_1': models_1,
            })
