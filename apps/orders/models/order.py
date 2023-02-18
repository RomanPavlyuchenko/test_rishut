from django.db import models

from ..models import Item
from .managers import OrderManager


class Order(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Название'
    )
    items = models.ManyToManyField(
        Item,
        related_name='orders',
        verbose_name='Товары',
    )

    objects = OrderManager()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self) -> str:
        return self.name
