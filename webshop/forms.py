from django import forms
from django.forms import ModelForm
from .models import Cart, Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields ='__all__'

