from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from product.models import Product, ProductImage

def order_contents(request):
    order_items = []
    total = 0
    product_count = 0
    overall_total = 0 
    item = request.session.get('item', {})
    images = ProductImage.objects.all()

    for books_id, order_data in item.items(): 
        if isinstance(order_data, int):
            product = get_object_or_404(Product, pk=books_id)
            total += order_data * product.price
            product_count += order_data
            order_items.append({
                'books_id': books_id,
                'quantity': order_data,
                'product': product,
                
            })

        delivery = total * Decimal(settings.DELIVERY_PERCENTAGE / 100)
        overall_total = total + delivery

    context = {
        "item_items": order_items,
        "total": total,
        "product_count": product_count,
        "images": images,
        "overall_total": overall_total,
    }

    return context
