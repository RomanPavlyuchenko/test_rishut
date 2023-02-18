from decimal import Decimal
import os

import stripe
from django.http import JsonResponse

DOMAIN_URL = 'http://127.0.0.1:8000/'
success_url = DOMAIN_URL + 'success.html'
cancel_url = DOMAIN_URL + 'cancel.html'


stripe.api_key = os.getenv('STRIPE_PRIVATE_KEY')


def checkout_create(price: Decimal, product_name: str, quantity=1) -> JsonResponse:
    session = stripe.checkout.Session.create(
        mode='payment',
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'inr',
                    'product_data': {
                        'name': product_name,
                    },
                    'unit_amount_decimal': price * 100,
                },
                'quantity': quantity,
            },
        ],
        success_url=success_url,
        cancel_url=cancel_url,
    )
    return session
