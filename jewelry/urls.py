from django.urls import path

from jewelry.views import customer, home

urlpatterns = [
    path('', home),
    path('customer/', customer)
]
