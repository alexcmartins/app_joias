from django.urls import path

from . import views

app_name = 'jewelry'

urlpatterns = [
    path('', views.home, name="home"),
    path('contacts/new/', views.newcontact, name="newcontact"),
    path('updatecontact/', views.updatecontact),
    path('login/', views.login, name="login"),
    path('jewelry/', views.jewelry, name="jewelry"),
    path('jewelry/<int:id>/', views.jewel, name="jewel"),
    path('jewelry/new/', views.newjewel, name="new"),
    path('updatejewel/', views.updatejewel),
    path('jewelry/settings/', views.settingsjewel, name="settings"),
]
