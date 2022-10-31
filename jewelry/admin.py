from django.contrib import admin

from .models import (CategoryJewelry, Contacts, Jewelry, ModelsJewelry,
                     TypesMetals, TypesPearls, TypesStones)


# Register your models here.
@admin.register(Contacts)
class ContactsAdmin(admin.ModelAdmin):
    ...


@admin.register(CategoryJewelry)
class CategoryJewelry(admin.ModelAdmin):
    ...


@admin.register(ModelsJewelry)
class ModelsJewelry(admin.ModelAdmin):
    ...


@admin.register(TypesMetals)
class TypesMetals(admin.ModelAdmin):
    ...


@admin.register(TypesStones)
class TypesStones(admin.ModelAdmin):
    ...


@admin.register(TypesPearls)
class TypesPearls(admin.ModelAdmin):
    ...


@admin.register(Jewelry)
class Jewelry(admin.ModelAdmin):
    ...
