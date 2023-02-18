from rest_framework import serializers

from ..models import Order
from ..serializers import ItemRetrieveSerializer


class OrderSerializer(serializers.ModelSerializer):
    items = ItemRetrieveSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'items')


class OrderAmountSerializer(serializers.ModelSerializer):
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    items = ItemRetrieveSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'name', 'items', 'amount')
