from django import forms

from sales_backend.models import Product

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductFrom(forms.Form):
    quantity = forms.IntegerField()
    update = forms.BooleanField(
        required=False,
        initial=False
    )

    # def clean_quantity(self):
    #     data = self.cleaned_data['artist']       
    #     if not Product.objects.filter(artist=data).exists():
    #         raise forms.ValidationError('Данного артиста нет!')           
    #     return data