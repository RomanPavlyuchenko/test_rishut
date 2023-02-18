from rest_framework.routers import DefaultRouter

from .viewsets import ItemViewSet, OrderViewSet

items_router = DefaultRouter()

items_router.register(
    prefix='items',
    viewset=ItemViewSet,
    basename='items'
)

items_router.register(
    prefix='orders',
    viewset=OrderViewSet,
    basename='orders'
)
