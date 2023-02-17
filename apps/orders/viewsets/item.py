from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from ..models import Item
from ..serializers import ItemRetrieveSerializer


class ItemViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        return Item.objects.all()

    def get_serializer_class(self):
        return ItemRetrieveSerializer
