from django.db.models import QuerySet, Sum, DecimalField
from django.db.models.functions import Coalesce


class OrderQuerySet(QuerySet):
    def annotate_amounts(self):
        return self.annotate(
            amount=Coalesce(
                Sum('items__price', distinct=True),
                0,
                output_field=DecimalField(),
            ),
        )
