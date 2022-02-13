from zoneinfo import available_timezones
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
# from django import req
from . import models, forms
from cart.forms import CartAddProductFrom

def main_page(request):
    template = 'sales_backend/main_page.html'
    products = models.ProductGroup.objects.all()
    return render(
        request,
        template,
        {'products': products}
    )

def product_group(request, slug):
    template = 'sales_backend/product_group.html'
    product = get_object_or_404(
        models.ProductGroup,
        slug=slug
    )
    return render(
        request,
        template,
        {'products': product.categroria.all()}
    )

def product_detail(request, id):
    template = 'sales_backend/product_detail.html'
    product = get_object_or_404(
        models.Product,
        pk=product_id
    )
    return render(
        request,
        template,
        {'product': product}
    )

def create_product(request):
    form = forms.ProductForm(request.POST or None)
    if form.is_valid():
        product = form.save(commit=False)
        product.save()
        return redirect('sales_backend:main_page')
    return render(
        request,
        'sales_backend/create_product.html',
        {'form': form}
    )

def product_detail(request, id):
    template = 'sales_backend/product_detail.html'
    product = get_object_or_404(
        models.Product,
        id=id,
        # slug=slug,
        # available=True
    )
    cart_product_form = CartAddProductFrom()
    return render(
        request,
        template,
        {
            "product": product,
            "cart_product_form": cart_product_form
        }
    )