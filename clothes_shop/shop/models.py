from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    Category for product
    """
    name = models.CharField(
        max_length=200,
        db_index=True,
        verbose_name='Имя категории товаров'
    )
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категория'

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    """
    The product
    """
    category = models.ForeignKey(Category, 
                                 related_name='products',
                                 on_delete=models.DO_NOTHING,
                                 verbose_name='Категория товара')
    name = models.CharField(max_length=200, db_index=True,
                            verbose_name='Имя товара')
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True,
                              verbose_name='Изображение товара')
    description = models.TextField(blank=True, verbose_name='Описание')
    price = models.DecimalField(max_digits=10, decimal_places=2,
                                verbose_name='Цена')
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True,
                                    verbose_name='Товар доступен для заказа')
    created = models.DateTimeField(auto_now_add=True,
                                   verbose_name='Дата публикации товара')
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления информации о товаре'
    )

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Продукт'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
