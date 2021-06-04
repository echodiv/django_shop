from django.shortcuts import redirect, get_object_or_404
from django.views.generic import View

from shop.models import Product

from .cart import Cart
from .forms import CartAddProductForm


class CartView(View):
    """
    Представление продуктовой корзины покупателя

    1. post для добавления товаров в корзину
    2. get соответственно для удаления
    """
    @staticmethod
    def post(request, product_id):
        """
        Добавление товара в корзину

        return: редирект на страницу корзины
        """
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cart.add(
                product=product,
                quantity=cleaned_data['quantity'],
                update_quantity=cleaned_data['update'],
                )
        return redirect('cart:cart_detail')

    @staticmethod
    def get(request, product_id):
        """
        Удаление товара из корзины.
        todo: delete http method

        return: редирект на страницу корзины
        """
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.remove(product)
        return redirect('cart:cart_detail')
