from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST

from shop.models import Product

from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    """
    add product to cart

    after adding redirect to cart detail page
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cleaned_data = form.cleaned_data
        cart.add(product=product,
                 quantity=cleaned_data['quantity'],
                 update_quantity=cleaned_data['update'],
                 )
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    """
    remove product from cart

    after remove: redirect to cart detail page
    """
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')
 

def cart_detail(request):
    """
    cart detail page
    """
    cart = Cart(request)
    return render(request, 'cart/details.html', {'cart': cart})
