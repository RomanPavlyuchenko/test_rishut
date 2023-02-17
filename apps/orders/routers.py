from rest_framework.routers import DefaultRouter

from .viewsets import ItemViewSet

items_router = DefaultRouter()

items_router.register(
    prefix='',
    viewset=ItemViewSet,
    basename='',
)
