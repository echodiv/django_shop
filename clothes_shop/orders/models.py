from django.db import models

from shop.models import Product


class Order(models.Model):
    """
    Содержит данные заказчика для доставки заказа
    """
    first_name = models.CharField(max_length=50, verbose_name='Имя заказчика')
    last_name = models.CharField(max_length=50,
                                 verbose_name='Фамилия заказчика')
    email = models.EmailField(verbose_name='eMail заказчика')
    address = models.CharField(max_length=250, verbose_name='Адрес заказчика')
    postal_code = models.CharField(max_length=20, verbose_name='Индекс')
    city = models.CharField(max_length=100, verbose_name='Город')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата совершения заказа')
    updated = models.DateTimeField(auto_now=True,
                                   verbose_name='Дата обновления заказа')
    paid = models.BooleanField(default=False, verbose_name='Оплата')

    class Meta:
        ordering = ('-created',)
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    """
    Содержит товары относящиеся к заказу
    """
    order = models.ForeignKey(Order, related_name='items',
                              verbose_name='Заказ',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name='Товар',
                                related_name='order_items', null=True,
                                on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена товара на момент заказа')
    quantity = models.PositiveIntegerField(
        default=1, verbose_name='Количество заказанных товаров')

    class Meta:
        verbose_name = 'Элемент заказа'

    def __str__(self):
        return f'Order item: {self.id}'

    def get_cost(self):
        """
        Возвращает суммарную стоимость товара в зависимости от количества
        """
        return self.price * self.quantity
