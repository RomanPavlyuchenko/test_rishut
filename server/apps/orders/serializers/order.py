from rest_framework import serializers

from ..models import Order
from ..serializers import ItemRetrieveSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = ItemRetrieveSerializer(many=True)
    tax = serializers.DecimalField(max_digits=5, decimal_places=2)
    discount = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Order
        fields = ('id', 'name', 'items', 'tax', 'discount')


class OrderAmountSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    items = ItemRetrieveSerializer(many=True)
    tax = serializers.DecimalField(max_digits=5, decimal_places=2)
    discount = serializers.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        model = Order
        fields = ('id', 'name', 'amount', 'items', 'tax', 'discount')
