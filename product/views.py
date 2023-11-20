from django.shortcuts import render
from .models import Product, ProductImage, Language, Category 
# Create your views here.

def show_book(request):

    books = Product.objects.all()
    language = Language.objects.all()
    images = ProductImage.objects.all()
    context = {
        'books': books,
        'images': images,
        'language': language,
    }
    return render(request, 'book/book.html', context)

def book_detail(request, book_id):

    book = get_object_or_404(Product, id=book_id)
    context = {
        'book': book
    }
    return render (request, 'book/book_detail.html', context)