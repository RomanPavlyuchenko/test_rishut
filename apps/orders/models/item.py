from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Item(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Товар'
    )
    description = models.TextField(
        verbose_name='Описание'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Стоимость',
        validators=(MinValueValidator(Decimal('0.01')),),
    )

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self) -> str:
        return self.name
