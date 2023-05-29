from django import forms
from catalog.models import Product


class UploadFileForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'image', 'price', 'category']
