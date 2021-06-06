from datetime import datetime

from django.test import TestCase
from django.core.exceptions import ValidationError

from ..models import Coupon


class CouponModelPositiveTestCases(TestCase):
    """
    Позитивные тесты модели данных описываюей купоны
    """
    def test_create_coupon_with_zero_discount(self):
        coupon = Coupon(
            code='123',
            valid_from=datetime.now(),
            valid_to=datetime.now(),
            discount=0,
            active=True
        )
        coupon.save()
        self.assertEqual(coupon.discount, 0,
                         'Discount is not equal to zero. Got {}'.format(
                             coupon.discount
                         ))

    def test_create_coupon_with_one_hundred_discount(self):
        coupon = Coupon(
            code='123',
            valid_from=datetime.now(),
            valid_to=datetime.now(),
            discount=100,
            active=True
        )
        coupon.save()
        self.assertEqual(coupon.discount, 100,
                         'Discount is not equal to one hundred. Got {}'.format(
                             coupon.discount
                         ))

    def test_coupon_with_fifty_symbols(self):
        coupon = Coupon(
            code='1' * 50,
            valid_from=datetime.now(),
            valid_to=datetime.now(),
            discount=10,
            active=True
        )
        coupon.save()
        self.assertEqual(len(coupon.code), 50,
                         'Discount is not equal to fifty. Got {}'.format(
                             len(coupon.code)
                         ))


class CouponModelNegativeTests(TestCase):
    """
    Негативные тесты модели данных описываюей купоны
    """
    def test_create_coupon_with_negative_discount(self):
        coupon = Coupon(
            code='abc',
            valid_from=datetime.now(),
            valid_to=datetime.now(),
            discount=-1,
            active=True
        )
        self.assertRaises(ValidationError, coupon.full_clean)

    def test_create_coupon_with_101_discount(self):
        coupon = Coupon(
            code='a123',
            valid_from=datetime.now(),
            valid_to=datetime.now(),
            discount=101,
            active=True
        )
        self.assertRaises(ValidationError, coupon.full_clean)

    def test_coupon_with_fifty_one_symbols(self):
        coupon = Coupon(
            code='a' * 51,
            valid_from=datetime.now(),
            valid_to=datetime.now(),
            discount=10,
            active=True
        )
        self.assertRaises(ValidationError, coupon.full_clean)
