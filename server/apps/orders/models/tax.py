from decimal import Decimal

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Tax(models.Model):
    percent = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Процент',
        validators=(
            MinValueValidator(Decimal('0.01')),
            MaxValueValidator(Decimal('100.00')),
        ),
        default=Decimal('0.00'),
    )

    class Meta:
        verbose_name = 'Налог'
        verbose_name_plural = 'Налоги'

    def __str__(self) -> str:
        return f'{self.percent}'
