from django.urls import path, include

from apps.orders.routers import items_router

urlpatterns = [
    path('orders/', include((items_router.urls, 'apps.orders'), namespace='orders')),
]
