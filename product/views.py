from django.shortcuts import render
from .models import Product, ProductImage, Language, Category 
# Create your views here.

def show_book(request):

    books = Product.objects.all()
    context = {
        'books': books
    }
    return render(request, 'book/book.html', context)