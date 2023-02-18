from django.db.models import Manager

from ..querysets import OrderQuerySet


class OrderManager(Manager):
    def get_queryset(self, **kwargs) -> OrderQuerySet:
        return OrderQuerySet(
            self.model,
            using=self._db,
        )

    def annotate_amounts(self):
        return self.get_queryset().annotate_amounts()
