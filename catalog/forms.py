from django import forms
from catalog.models import Product, Version, Post

STOP_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'image', 'price', 'category')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        check_words(cleaned_data)
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description']
        check_words(cleaned_data)
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def clean_is_active(self):
        cleaned_data = self.cleaned_data['is_active']
        product = self.cleaned_data['product']
        is_active_version_exists = Version.objects.filter(product=product, is_active=True).exists()
        if cleaned_data and is_active_version_exists:
            raise forms.ValidationError('Уже есть активная версия')
        return cleaned_data


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'preview', 'published')


def check_words(data):
    for word in STOP_WORDS:
        if word in data:
            raise forms.ValidationError(f'Недопустимое слово: {word}')
