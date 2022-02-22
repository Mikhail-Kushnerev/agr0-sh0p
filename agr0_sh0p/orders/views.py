from django.shortcuts import render
from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    
    form = OrderCreateForm(request.POST or None)
    if form.is_valid():
        order = form.save()
        # order.user = request.user
        for item in cart:
            OrderItem.objects.create(
                order=order,
                user=request.user,
                seller=item['product'].user,
                product=item['product'],
                price=item['total_price'],
                quantity=item['quantity']
            )
        # очистка корзины
        cart.clear()
        return render(
            request,
            'orders/success.html',
            {'order': order}
        )
    return render(
        request,
        'orders/create.html',
        {
            'cart': cart,
            'form': form
        }
    )