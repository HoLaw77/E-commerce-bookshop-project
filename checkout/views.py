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
        "confirm_order": confirm_order
    }

    return render (request, template, context)