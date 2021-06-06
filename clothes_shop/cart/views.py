from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from shop.models import Product
from coupons.forms import CouponApplyForm

from .cart import Cart
from .forms import CartAddProductForm


class CartManagerView(View):
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


class CartView(View):
    """
    Представление корзины с учётом примененного скидочного купона
    """
    @staticmethod
    def get(request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(
                initial={
                    'quantity': item['quantity'],
                    'update': True,
                }
            )
        coupon_apply_form = CouponApplyForm()
        return render(request, 'cart/details.html',
                      {'cart': cart, 'coupon_apply_form': coupon_apply_form})
