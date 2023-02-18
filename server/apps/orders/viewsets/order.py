from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from ..models import Order
from ..models.querysets import OrderQuerySet
from ..serializers import OrderAmountSerializer
from payments import checkout_create


class OrderViewSet(viewsets.ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self) -> OrderQuerySet:
        return Order.objects.get_queryset().annotate_amounts()

    def get_serializer_class(self, *args, **kwargs):
        return OrderAmountSerializer

    @action(methods=('GET',), detail=False, url_path='buy/(?P<pk>[^/.])',)
    def get_checkout_id(self, request: Request, pk=None) -> Response:
        obj = self.get_object()
        session = checkout_create(obj.amount, obj.name)
        return JsonResponse({'id': session.id})

    @action(methods=('GET',), detail=False, url_path='pay/(?P<pk>[^/.]+)',)
    def get_payment_page(self, request: Request, pk=None) -> Response:
        obj = self.get_object()
        data = OrderAmountSerializer(obj).data
        return Response(
            {
                'name': data['name'],
                'amount': data['amount'],
                'id': pk
            },
            template_name='payment_order.html'
        )
