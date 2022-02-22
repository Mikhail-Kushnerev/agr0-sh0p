from importlib.metadata import files
from zoneinfo import available_timezones
from django.shortcuts import redirect, render
from django.shortcuts import get_object_or_404
from django.forms import modelformset_factory

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

def create_product(request):
    button = 'Добавить товар'
    form = forms.ProductForm(request.POST or None)
    formset = forms.ProductImagesForm(
        request.POST or None,
        files=request.FILES or None
    )
    if form.is_valid() and formset.is_valid():
        product = form.save(commit=False)
        product.user = request.user
        product.save()

        for pic in request.FILES.getlist('image'):
            photo = models.ProductImages(
                image=pic,
                product=product
            )
            photo.save()
        return redirect('sales_backend:main_page')
    return render(
        request,
        'sales_backend/create_product.html',
        {
            'form': form,
            'formset': formset,
            'button': button,
        }
    )

def product_detail(request, id):
    template = 'sales_backend/product_detail.html'
    product = get_object_or_404(
        models.Product,
        id=id,
        # slug=slug,
        # available=True
    )
    product_images = product.images.all()
    form = forms.CommentForm()
    comments = models.CommentProduct.objects.filter(product=product)
    cart_product_form = CartAddProductFrom()
    return render(
        request,
        template,
        {
            "product": product,
            "product_images": product_images[1:],
            "preview": product_images[0].image,
            'form': form,
            "count": product.count,
            "cart_product_form": cart_product_form,
            "comments": comments,
        }
    )

def edit_product(request, id):
    button = 'Сохранить изменения'
    product_user = get_object_or_404(
        models.Product,
        id=id
    )
    form = forms.ProductForm(
        request.POST or None,
        instance=product_user,
    )
    if form.is_valid():
        product_edit = form.save()
        product_edit.user = request.user
        product_edit.save()
        return redirect(
            'sales_backend:product_detail',
            id=id
        )
    return render(
        request,
        'sales_backend/create_product.html',
        {
            'form': form,
            'button': button,
        }
    )


def addcomment(request, id):
    product = get_object_or_404(
        models.Product,
        id=id
    )
    form = forms.CommentForm(request.POST or None)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.product=product
        comment.save()
    return redirect(
        'sales_backend:product_detail',
        id=id
    )
