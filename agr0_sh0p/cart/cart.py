from decimal import Decimal
from django.conf import settings
from sales_backend.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохраняем ПУСТУЮ корзину в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        """
        Перебираем товары в корзине и получаем товары из базы данных.
        """
        product_ids = self.cart.keys()
        # получаем товары и добавляем их в корзину
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['count'] = int(item['count'])
            if item['quantity'] > product.count:
                item['total_price'] = item['price'] * item['count']
            else:
                item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        """
        Считаем сколько товаров в корзине
        """
        return sum(item['quantity'] for item in self.cart.values())

    def add(
        self,
        product,
        count,
        quantity=1,
        update_quantity=False
    ):
        """
        Добавляем товар в корзину или обновляем его количество.
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': 0,
                'count': str(count),
                'price': str(product.price)
            }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # сохраняем товар
        # self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def decrement(request, id):
        if request.method == "GET":
            item = Product.objects.get(id=id)
            if 0 < (item.quantity - 1) <= item.prod_id.quantity:
                item.quantity -= 1
                item.save()
        #         return redirect('cart')
        # return redirect('cart')

    def remove(self, product):
        """
        Удаляем товар
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        # получаем общую стоимость
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        # очищаем корзину в сессии
        del self.session[settings.CART_SESSION_ID]
        self.save()