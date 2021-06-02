from django.shortcuts import render, get_object_or_404

from cart.forms import CartAddProductForm

from .models import Product, Category


def product_list(request, category_slug=None):
    """
    Get products with category or wothout
    """
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    """
    Get product with id and slug
    """
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 
                  'shop/product/details.html',
                  {'product': product, 
                   'cart_product_form': cart_product_form})