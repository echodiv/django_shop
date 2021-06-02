from decimal import Decimal

from django.conf import settings

from shop.models import Product


class Cart:
    def __init__(self, request):
        """
        Cart initialization

        save data in user session
        """
        self.session = request.session

        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        
        self.cart = cart
    
    def add(self, product, quantity=1, update_quantity=False):
        """
        add new product to cart
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity': quantity,
                'price': str(product.price),
                }
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        
        self.save()

    def save(self):
        """
        save changes in user session cart storage
        """
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True

    def remove(self, product):
        """
        remove product from cart
        """
        product_id = str(product.id)
        # TODO: if product_id not in self.cart
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def get_total_price(self):
        """
        get summary price of all products in cart
        """
        return sum(Decimal(item['price']) * item ['quantity'] 
                   for item in self.cart.values())
    
    def clear(self):
        """
        delete cart from session storage
        """
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True
    
    def __iter__(self):
        for product in Product.objects.filter(id__in=self.cart.keys()):
            self.cart[str(product.id)]['product'] = product
        
        for item in self.cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item
    
    def __len__(self):
        return sum([item['quantity'] for item in self.cart.values()])
