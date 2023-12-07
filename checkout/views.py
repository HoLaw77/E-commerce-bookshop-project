from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.conf import settings
from .forms import ConfirmOrder
from .models import Order, OrderDetail
from order.contexts import order_contents
from product.models import Product
import stripe
# Create your views here.

def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == "POST":
        item = request.session.get('item', {})
        form_data = {
        "full_name": request.POST["full_name"],  
        "email": request.POST["email"], 
        "phone_number": request.POST["phone_number"], 
        "address1": request.POST["address1"], 
        "address2": request.POST["address2"], 
        "postcode": request.POST["postcode"], 
        "countries": request.POST["countries"],
        }

        confirm_order = ConfirmOrder(form_data)
        if confirm_order.is_valid():
            order = confirm_order.save()
            
            for books_id, order_data in item.items():
                try: 
                    product = Product.objects.get(id=books_id)
                    if isinstance(order_data, int):
                        order_detail = OrderDetail(
                            order=order,
                            product=product,
                            quantity= order_data,
                        )
                        order_detail.save()

                except Product.DoesNotExist:
                    order.delete()
                    return redirect(reverse('show_order'))
            request.session["save-info"] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', 
            args=[order.order_number]))
        else:
            message.error("Error with the inforamtion provided, please check the form.")

            
    else:

        item = request.session.get('item', {})
        if not item:
            # message.error(request, "No book in your cart now.")
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


def checkout_success(request, order_number):
    """Handle request when checkout successfully"""

    save_info = request.session.get("save-info")
    order = get_object_or_404(Order, order_number = order_number)
    # message.success(request, 
    # f'Order successfully processed. Order number is {order_number}. \
    # A confirmation email will be send to {order.email}')

    if 'item' in request.session:
        del request.session['item']
        

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_number': order_number
    }

    return render (request, template, context) 