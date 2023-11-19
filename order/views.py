from django.shortcuts import render

# Create your views here.
def show_order(request):

    return render (request, 'order/order.html')