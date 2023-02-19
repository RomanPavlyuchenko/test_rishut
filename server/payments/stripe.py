import os

import stripe
from django.http import JsonResponse


DOMAIN_URL = 'http://127.0.0.1:8000/'
success_url = DOMAIN_URL + 'success.html'
cancel_url = DOMAIN_URL + 'cancel.html'

stripe.api_key = os.getenv('STRIPE_PRIVATE_KEY')


def checkout_create(price=1, tax_rate=None, name='Some order',
                    quantity=1, discount=0.00) -> JsonResponse:

    params = {
        'mode': 'payment',
        'payment_method_types': ['card'],
        'success_url': success_url,
        'cancel_url': cancel_url,
        'line_items': [
            {
                'price_data': {
                    'currency': 'usd',
                    'product_data': {
                        'name': name,
                    },
                    'unit_amount_decimal': price * 100,
                },
                'quantity': quantity,
            }
        ]
    }

    if tax_rate:
        params['line_items'][0]['tax_rates'] = [_get_tax_id(tax_rate)]
    if discount:
        params['discounts'] = [{'coupon': _get_discount_id(discount)},]

    return stripe.checkout.Session.create(**params)


def _get_discount_id(percent_off=0) -> str:
    disc = stripe.Coupon.create(percent_off=percent_off, duration="once")
    return disc.id


def _get_tax_id(percentage=0.00) -> str:
    return stripe.TaxRate.create(
        display_name="Sales Tax",
        inclusive=False,
        percentage=percentage
    ).id
