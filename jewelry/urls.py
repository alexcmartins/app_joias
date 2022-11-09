from django.urls import path

from . import views

app_name = 'jewelry'

urlpatterns = [
    path('', views.home, name="home"),
    path('login', views.login, name="login"),
    path('jewelry', views.jewelry, name="jewelry"),
    path('contacts/new', views.new_contact, name="new-contact"),
    path('contacts/<int:id>', views.contact, name="contact"),
    path('contacts/update/<int:id>', views.update_contact,
         name="update-contact"),
    path('jewelry/new', views.new_jewel, name="new-jewel"),
    path('jewelry/<int:id>', views.jewel, name="jewel"),
    path('jewelry/update/<int:id>', views.update_jewel, name="update-jewel"),
    path('jewelry/settings', views.settings_jewel, name="settings-jewel"),
]
