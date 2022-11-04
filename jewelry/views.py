from django.db.models import Q
from django.shortcuts import redirect, render

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


def new_contact(request):
    return render(request, 'jewelry/pages/newcontact.html')


def new_contact_save(request):
    if request.method == "POST":
        first_name = request.POST.get("inputFirstName")
        last_name = request.POST.get("inputFirstName")
        email = request.POST.get("inputFirstName")
        company = request.POST.get("inputFirstName")
        birthday = request.POST.get("inputFirstName")
        instagram = request.POST.get("inputFirstName")
        whatsapp = request.POST.get("inputFirstName")
        mobile = request.POST.get("inputFirstName")
        house_office = request.POST.get("inputFirstName")
        image_contact = request.POST.get("inputFirstName")
        address = request.POST.get("inputFirstName")
        notes = request.POST.get("inputFirstName")

        Contacts(
            first_name=first_name,
            last_name=last_name,
            email=email,
            company=company,
            birthday=birthday,
            instagram=instagram,
            whatsapp=whatsapp,
            mobile=mobile,
            house_office=house_office,
            image_contact=image_contact,
            address=address,
            notes=notes,
        ).save()

    return redirect('jewelry/pages/home.html')


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
