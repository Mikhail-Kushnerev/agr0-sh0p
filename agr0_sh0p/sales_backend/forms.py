from django import forms

from .models import (
    Product,
    ProductImages,
    CommentProduct
)



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

        widgets = {
            'name': forms.TextInput(attrs={'size': '40'}),
        }


class ProductImagesForm(forms.ModelForm):
    # image = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    class Meta:
        model = ProductImages
        fields = ['image']

        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': True}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = CommentProduct
        fields = ('text', )