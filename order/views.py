from django.shortcuts import render

# Create your views here.
def show_order(request):

    return render (request, 'order/order.html')

def add_order(request, product_id):
    """Add order to cart"""

    book = get_object_or_404(Product, pk=product_id)
    quantity = int(request.POST.get('quantity'))
    order = request.session.get('order', {})

    if product_id in list(order.keys()):
        order[product_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {order[product_id]}')
    else:
        order[product_id] = quantity
        messages.success(request, f'Added {product.name} to cart')

    request.session['order'] = order
    print(order)
    return redirect(redirect_url)
