from django.contrib import admin

from ..models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'order_items', 'amount')

    def order_items(self, obj):
        return ", ".join([p.name for p in obj.items.all()])

    def amount(self, obj):
        amount = 0
        for p in obj.items.all():
            amount += p.price
        return amount
