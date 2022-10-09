from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')


def customer(request):
    return HttpResponse('Welcome Client!')
