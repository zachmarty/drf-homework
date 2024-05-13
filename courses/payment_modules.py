import stripe

from config import settings
from rest_framework.reverse import reverse_lazy

stripe.api_key = settings.STRIPE_API_KEY


def create_payment_product(name, description):
    product = stripe.Product.create(name=name, description=description)
    return product


def create_payment_price(price, product_id):
    price = stripe.Price.create(
        currency="rub",
        unit_amount=price * 100,
        product=product_id,
    )
    return price


def create_payment_session(price_id, payment_id, request):
    session = stripe.checkout.Session.create(
        line_items=[
            {
                "price": price_id,
                "quantity": 1,
            }
        ],
        mode="payment",
        success_url=reverse_lazy(
            "courses:payment_detail",
            kwargs={"pk": payment_id},
            request=request,
        ),
    )
    return session

def get_session_info(session_id):
    session = stripe.checkout.Session.retrieve(
        session_id
    )
    return session
