from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from product.models import Product, ProductImage

def order_contents(request):
    order_items = []
    total = 0
    product_count = 0 
    order = request.session.get('order', {})
    images = ProductImage.objects.all()

    for books_id, order_data in order.items(): 
        if isinstance(order_data, int):
            product = get_object_or_404(Product, pk=books_id)
            total += order_data * product.price
            product_count += order_data
            order_items.append({
                'books_id': books_id,
                'quantity': order_data,
                'product': product,
                
            })
    context = {
        "order_items": order_items,
        "total": total,
        "product_count": product_count,
        "images": images,
    }

    return context
