from django.shortcuts import render, redirect
from .models import Order, OrderDetail
# Create your views here.
def show_order(request):

    return render (request, 'order/order.html')

def add_order(request, book_id):
    """Add individual book to cart"""
    product = get_object_or_404(Product, id=book_id)
    redirect_url = request.POST.GET('redirect_url')
    order = request.session.get('order', {})

    if book_id in list(order.keys()):
        order[book_id].create()
        messages.success(request, f'Added {product.name} to cart')
    else: 
        return reverse(book_detail)
    request.session['order'] = order
    print(order)
    return redirect(redirect_url)

    