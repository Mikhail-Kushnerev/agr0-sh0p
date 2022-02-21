from django import forms

from .models import Product, CommentProduct


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
            'name',
            'group',
            'price',
            'description',
            'count'
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentProduct
        fields = ('text', )