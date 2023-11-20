from django.shortcuts import render
from .models import Product, ProductImage, Language, Category 
from django.shortcuts import get_object_or_404
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

    books = get_object_or_404(Product, id=book_id)
    images = ProductImage.objects.all()
    categories = Category.objects.all()
    language = Language.objects.all()
    context = {
        'books': books,
        'images': images,
        'categories': categories,
        'language': language,
    }
    return render (request, 'book/book_detail.html', context)