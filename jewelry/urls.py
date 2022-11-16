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
    path('contacts/delete/<int:id>', views.delete_contact,
         name="delete-contact"),
    path('jewelry/new', views.new_jewel, name="new-jewel"),
    path('jewelry/<int:id>', views.jewel, name="jewel"),
    path('jewelry/update/<int:id>', views.update_jewel, name="update-jewel"),
    path('jewelry/settings', views.settings_jewel, name="settings-jewel"),
    path('jewelry/settings/indicators/update/<int:id>',
         views.update_indicators, name="update-indicators"),
    path('jewelry/settings/indicators/delete/<int:id>',
         views.delete_indicators, name="delete-indicators"),
    path('jewelry/settings/category/update/<int:id>',
         views.delete_indicators, name="update-category"),
    path('jewelry/settings/category/delete/<int:id>',
         views.delete_indicators, name="delete-category"),
    path('jewelry/settings/models/update/<int:id>',
         views.delete_indicators, name="update-models"),
    path('jewelry/settings/models/delete/<int:id>',
         views.delete_indicators, name="delete-models"),
]
