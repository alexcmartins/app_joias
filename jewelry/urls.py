from django.urls import path

from . import views

urlpatterns = [
    path('', views.home),
    path('contact/', views.contact),
    path('login/', views.login),
    path('jewel/', views.jewel),
    path('newjewel/', views.newjewel),
    path('updatejewel/', views.updatejewel),
    path('settingsjewel/', views.settingsjewel),
]
