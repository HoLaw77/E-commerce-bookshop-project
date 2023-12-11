from django.shortcuts import render, redirect, reverse
from django.shortcuts import HttpResponse, get_object_or_404
from product.models import Product, ProductImage


# Create your views here.
def show_order(request):
    # products = Products.objects.all()
    # print('request', request)

    # return render (request, 'order/order.html', products)
    bag = request.session.get('bag', {})

    return render (request, 'order/order.html', bag)

def add_order(request, books_id):
    """Add individual book to cart"""
    # books_id = request.POST.get('books_id')
    print("books_id", books_id)
    product = get_object_or_404(Product, id=books_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    print(bag)
    item_items = bag.get('item_items')
    print('item_items', item_items)
    print('product: ', product)
    print("quantity: ", quantity)
    # print("bag: ", bag['item_items'])
    print("!!!!!!!!!")
    print(bag)
    print(bag)
    print("list(bag.keys())", list(bag.keys()))

    # if not str(books_id) in list(bag.keys()):
    bag[books_id] = quantity
    #     print("Yes it is in the bag")
    #     bag[str(books_id)]+= quantity
    #     print("bag", bag)

    #     # messages.success(request, f'Added {product.name} to cart')
    # else: 
    #     print("Nooooo")
    request.session['bag'] = bag
    
    print(bag)
    
    
    request.session['bag'] = bag
    print(request.session['bag'])

    # return render (request, "order/order.html")
    context = {
        'order_items': request.session['bag']
    }

    return render (request, 'order/order.html', context)


def adjust_order(request, item_id):
    """Adjust quantity for individual book to cart"""
    
    quantity = int(request.POST.get('quantity'))
    print("line62")
    bag = request.session['bag']
    print("Line 63!!!!bag",bag)
    if request.method == "POST":
        if quantity > 0:
            bag[item_id] = quantity
            # messages.success(request, f'Adjusted {product.name} quantity')
            return render (request, 'order/order.html')
        else: 
            item.pop(item_id)
        request.session['bag'] = bag
    return redirect(reverse('show_order'))


def remove_order(request, item_id):
    """Remove individual product from the cart"""
    product = get_object_or_404(Product, id=item_id)

    request.session['bag'] = {}
    # item = request.session.get('item', {})
    # item
    # item.pop(item_id)
    # messages.success(request, f'Removed {product.name} from your cart')

    # request.session['item'] = item
    return HttpResponse(status=200)


def remove_all(request):
    print("enter remove all")
    # request.session['bag'] = bag
    bag = request.session.get('bag', {})
    print('!!!!REMOVE ALL BAG', bag)
    bag.clear()
    request.session.modified = True
    request.session['bag'] = bag

    return render (request, 'order/order.html')