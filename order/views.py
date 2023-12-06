from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from product.models import Product, ProductImage

# Create your views here.
def show_order(request):
    image = ProductImage.objects.all()
    print('request', request)
    
    

    return render (request, 'order/order.html')

def add_order(request, books_id):
    """Add individual book to cart"""
    product = get_object_or_404(Product, id=books_id)
    quantity = int(request.POST.get('quantity'))
    item = request.session.get('item', {})
    print('product: ', product)
    print("quantity: ", quantity)
    print("item: ", item)
    

    if books_id in list(item.keys()):
        item[books_id]+= quantity
        messages.success(request, f'Added {product.name} to cart')
    else: 
        item[books_id] = quantity
    request.session['item'] = item
    
    print(item)
    
    
    request.session['item'] = item
    print(request.session['item'])

    # return render (request, "order/order.html")
    context = {
        'order_items': request.session['item']
    }

    return render (request, 'order/order.html', context)


def adjust_order(request, item_id):
    """Adjust quantity for individual book to cart"""
    
    quantity = int(request.POST.get('quantity'))
    item = request.session.get('item', {})
    if request.method == "POST":
        if quantity > 0:
            item[item_id] = quantity
            messages.success(request, f'Adjusted {product.name} quantity')
            return render (request, 'order/order.html')
        else: 
            item.pop(item_id)
        request.session['item'] = item
    return redirect(reverse('show_order'))


def remove_order(request, item_id):
    """Remove individual product from the cart"""
    product = get_object_or_404(Product, id=item_id)
    item = request.session.get('item', {})
    item.pop(item_id)
    messages.success(request, f'Removed {product.name} from your cart')

    request.session['item'] = item
    return HttpResponse(status=200)
    