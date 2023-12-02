from django.shortcuts import render, redirect, reverse
from .models import Order, OrderDetail
from django.shortcuts import HttpResponse, get_object_or_404
from product.models import Product

# Create your views here.
def show_order(request):

    return render (request, 'order/order.html')

def add_order(request, books_id):
    """Add individual book to cart"""
    product = get_object_or_404(Product, id=books_id)
    quantity = int(request.POST.get('quantity'))
    order = request.session.get('order', {})
    

    if books_id in list(order.keys()):
        order[books_id]+= quantity
        messages.success(request, f'Added {product.name} to cart')
    else: 
        order[books_id] = quantity
    request.session['order'] = order
    
    print(order)
    
    
    request.session['order'] = order
    return render (request, "order/order.html")

def adjust_order(request, books_id):
    """Adjust quantity for individual book to cart"""
    product = get_object_or_404(Product, id=books_id)
    quantity = int(request.POST.get('quantity'))
    order = request.session.get('order', {})
    

    if books_id in list(order.keys()):
        order[books_id]+= quantity
        messages.success(request, f'Added {product.name} to cart')
    else: 
        order[books_id] = quantity
    request.session['order'] = order
    
    print(order)
    
    
    request.session['order'] = order
    return render (request, "order/order.html")

def remove_order(request, books_id):
    """Remove individual product from the cart"""
    product = get_object_or_404(Product, id=books_id)
    order = request.session.get('order', {})
    order.pop(books_id)
    messages.success(request, f'Removed {product.name} from your cart')

    request.session['order'] = order
    return HttpResponse(status=200)
    