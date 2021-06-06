from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Coupon(models.Model):
    """
    Модель для хранения скидочных купонов
    """
    code = models.CharField(max_length=50, unique=True,
                            verbose_name='Код купона')
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    discount = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    active = models.BooleanField()

    class Meta:
        verbose_name = 'Скидочные купоны'

    def __str__(self):
        return f'Coupon: {self.code}'
