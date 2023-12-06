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
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount = stripe_total,
        currency = settings.STRIPE_CURRENCY,
    )

    print(intent)
    
    confirm_order = ConfirmOrder()

    # if not stripe_public_key:
    #     message.warning(request, 'You forget to set your stripe public key.')

    template = "checkout/checkout.html"
    context = {
        "confirm_order": confirm_order,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
    }

    return render (request, template, context)