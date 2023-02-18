from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Item
from ..serializers import ItemRetrieveSerializer
from payments import checkout_create


class ItemViewSet(viewsets.ModelViewSet):
    serializer_class = ItemRetrieveSerializer
    filter_backends = (DjangoFilterBackend,)
    renderer_classes = [TemplateHTMLRenderer]

    def get_queryset(self):
        queryset = Item.objects.all()
        return queryset

    def get_object(self) -> Item:
        return super().get_object()

    @action(methods=('GET',), detail=False, url_path='buy/(?P<pk>[^/.]+)',)
    def get_checkout_id(self, request: Request, pk=None) -> Response:
        obj = self.get_object()
        session = checkout_create(obj.price, obj.name)
        return JsonResponse({'id': session.id})

    @action(methods=('GET',), detail=False, url_path='item/(?P<pk>[^/.]+)',)
    def get_payment_page(self, request: Request, pk=None) -> Response:
        obj = self.get_object()
        return Response(
            {
                'name': obj.name,
                'description': obj.description,
                'price': obj.price,
                'id': obj.pk,
            },
            template_name='payments.html'
        )
