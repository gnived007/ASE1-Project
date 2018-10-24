from django import forms
from vendor.models import Product, Category


class ProductsAdd(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

