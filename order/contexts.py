from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from product.models import Product

def order_contents(request):
    order_items = []
    total = 0
    product_count = 0 
    order = request.session.get('order', {})

    for order_id, order_data in order.items(): 
        if isinstance(order_data, int):
            product = get_object_or_404(Product, pk=order_id)
            total += order_data * product.price
            product_count += order_data
            bag_items.append({
                'order_id': order_id,
                'quantity': order_data,
                'product': product,
            })
    context = {
        "order_items": order_items,
        "total": total,
        "product_count": product_count,
    }

    return context
