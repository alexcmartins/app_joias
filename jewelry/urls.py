from django.urls import path

from . import views

app_name = 'jewelry'

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('jewelry/', views.jewelry, name="jewelry"),
    path('contacts/new/', views.newcontact, name="newcontact"),
    path('contacts/<int:id>/', views.contact, name="contact"),
    path('contacts/<int:id>/update/', views.updatecontact, name="updatecontact"),
    path('jewelry/new/', views.newjewel, name="new"),
    path('jewelry/<int:id>/', views.jewel, name="jewel"),
    path('jewelry/<int:id>/update/', views.updatejewel),
    path('jewelry/settings/', views.settingsjewel, name="settings"),
]
