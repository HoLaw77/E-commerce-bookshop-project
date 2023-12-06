from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from .forms import ConfirmOrder
from order.contexts import order_contents

import stripe
# Create your views here.

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    item = request.session.get('item', {})
    if not item:
        message.error(request, "No book in your cart now.")
        return redirect(reverse('book'))
    order_in_cart = order_contents(request)
    total = order_in_cart['overall_total']
    stripe_total = round(total * 100) 
    stripe_api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = stripe_total,
        currency = settings.STRIPE_CURRENCY,
    )

    print(intent)
    
    confirm_order = ConfirmOrder()
    template = "checkout/checkout.html"
    context = {
        "confirm_order": confirm_order,
        "stripe_public_key": "pk_test_51OBjadE3mV0w6kupavap87LqckacfKyC4ua4w0lRjpFAnE8Zw33chnsmtOM9YUKp8NDYue3m3K4hAjMlYPUZ2qtn00CxCrEP1G",
        "client_secret": "client secret",
    }

    return render (request, template, context)