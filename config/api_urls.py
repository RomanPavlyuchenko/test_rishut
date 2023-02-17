from django.urls import path, include

from apps.orders.routers import items_router

urlpatterns = [
    path('items/', include(items_router.urls)),
]
