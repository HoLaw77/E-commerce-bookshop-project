def order_contents(request):
    order_items = []
    total = 0
    product_count = 0 
    context = {
        "order_items": order_items,
        "total": total,
        "product_count": product_count,
    }

    return context
