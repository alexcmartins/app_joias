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
         views.update_category_settings, name="update-category-settings"),
    path('jewelry/settings/category/delete/<int:id>',
         views.delete_category_settings, name="delete-category-settings"),
    path('jewelry/settings/models/update/<int:id>',
         views.update_models_settings, name="update-models-settings"),
    path('jewelry/settings/models/delete/<int:id>',
         views.delete_models_settings, name="delete-models-settings"),
    path('jewelry/settings/stones/update/<int:id>',
         views.delete_stones_settings, name="update-stones-settings"),
    path('jewelry/settings/stones/delete/<int:id>',
         views.delete_stones_settings, name="delete-stones-settings"),
    path('jewelry/settings/pearls/update/<int:id>',
         views.delete_pearls_settings, name="update-pearls-settings"),
    path('jewelry/settings/pearls/delete/<int:id>',
         views.delete_pearls_settings, name="delete-pearls-settings"),
    path('teste/', views.teste, name="teste"),
]
