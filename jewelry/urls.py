from django.urls import path

from jewelry.views import contact, home, jewel, login

urlpatterns = [
    path('', home),
    path('contact/', contact),
    path('login/', login),
    path('jewel/', jewel)
]
