from django import forms

from . import models


# Create Form Contact
class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contacts
        fields = "__all__"


# Create Forms Settings Jewelry
class IndicatorsForm(forms.ModelForm):
    class Meta:
        model = models.Indicators
        fields = "__all__"


class CategoryJewelryForm(forms.ModelForm):
    class Meta:
        model = models.CategoryJewelry
        fields = "__all__"


class ModelsJewelryForm(forms.ModelForm):
    class Meta:
        model = models.ModelsJewelry
        fields = "__all__"


class TypesMetalsForm(forms.ModelForm):
    class Meta:
        model = models.TypesMetals
        fields = "__all__"


class TypesStonesForm(forms.ModelForm):
    class Meta:
        model = models.TypesStones
        fields = "__all__"


class TypesPearlsForm(forms.ModelForm):
    class Meta:
        model = models.TypesPearls
        fields = "__all__"
