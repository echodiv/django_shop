from django.contrib.sessions.middleware import SessionMiddleware
from django.conf import settings
from django.test import TestCase
from django.test.client import RequestFactory

from shop.models import Product, Category

from .cart import Cart


class CartTestCases(TestCase):
    def setUp(self) -> None:
        Category.objects.create(name='test_name', slug='test_slug')
        test_category = Category.objects.get(name='test_name')
        Product.objects.create(
            category=test_category,
            name='test_product',
            slug='test_p_slug',
            price=5,
            stock=1,
        )
        self.factory = RequestFactory()

    def tearDown(self) -> None:
        product = Product.objects.filter(name='test_product')
        category = Category.objects.filter(name='test_name')
        product.delete()
        category.delete()

    @staticmethod
    def setup_request(request):
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()

    def test_add_product_to_cart(self):
        request = self.factory.post('/')
        self.setup_request(request)

        cart = Cart(request)
        product = Product.objects.get(name='test_product')
        cart.add(product=product)
        assert str(product.id) in cart.cart, \
            'No expected data in session'
        assert cart.cart[str(product.id)]['quantity'] == 1, \
            'Expect 1 instance of product, got {}'.format(
                cart.cart[str(product.id)]['quantity']
            )

    def test_add_two_instance_of_product(self):
        request = self.factory.post('/')
        self.setup_request(request)

        cart = Cart(request)
        product = Product.objects.get(name='test_product')
        cart.add(product=product, quantity=2)
        assert cart.cart[str(product.id)]['quantity'] == 2, \
            'Expect 2 instance of product, got {}'.format(
                cart.cart[str(product.id)]['quantity']
            )

    def test_add_and_remove_product_in_cart(self):
        request = self.factory.post('/')
        self.setup_request(request)

        cart = Cart(request)
        product = Product.objects.get(name='test_product')
        cart.add(product=product)
        cart.remove(product)
        assert str(product.id) not in cart.cart, \
            'Product founded in cart'

    def test_get_total_price_of_cart(self):
        request = self.factory.post('/')
        self.setup_request(request)

        cart = Cart(request)
        product = Product.objects.get(name='test_product')
        cart.add(product=product,
                 quantity=5)
        assert product.price * 5 == cart.get_total_price(), \
            'Total price is not correct'

    def test_clear_cart(self):
        request = self.factory.post('/')
        self.setup_request(request)

        cart = Cart(request)
        product = Product.objects.get(name='test_product')
        cart.add(product=product,
                 quantity=5)
        cart.clear()
        assert settings.CART_SESSION_ID not in cart.cart, \
            'Cart found in session'
