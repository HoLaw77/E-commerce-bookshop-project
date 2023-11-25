from django.shortcuts import render, redirect

# Create your views here.
def show_order(request):

    return render (request, 'order/order.html')

def add_order(request, book_id):
    """Add order to cart"""

    redirect_url = request.POST.GET('redirect_url')
    order = Order.objects.create()

    if book_id in list(order.keys()):
        order[book_id].create()
        messages.success(request, f'Added {product.name} to cart')
    else: 
        return redirect(book_detail)
    request.session['order'] = order
    print(order)
    
    return redirect(book_detail)