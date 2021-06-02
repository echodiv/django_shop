from .cart import Cart


def cart(request):
    """
    contgext processor for display cart on all pages
    """
    return {'cart': Cart(request)}
