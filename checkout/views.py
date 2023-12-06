from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import ConfirmOrder
# Create your views here.

def checkout(request):
    item = request.session.get('item', {})
    if not item:
        message.error(request, "No book in your cart now.")
        return redirect(reverse('book'))

    confirm_order = ConfirmOrder()
    template = "checkout/checkout.html"
    context = {
        "confirm_order": confirm_order,
        "stripe_public_key": "pk_test_51OBjadE3mV0w6kupavap87LqckacfKyC4ua4w0lRjpFAnE8Zw33chnsmtOM9YUKp8NDYue3m3K4hAjMlYPUZ2qtn00CxCrEP1G",
        "client_secret": "client secret",
    }

    return render (request, template, context)