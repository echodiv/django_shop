from .cart import Cart


def cart(request):
    """
    context processor for display cart on all pages
    """
    return {'cart': Cart(request)}
