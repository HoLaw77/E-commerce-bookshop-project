from django.shortcuts import render, redirect, reverse
from .models import Product, ProductImage, Language, Category 
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def show_book(request):

    books = Product.objects.all()
    query = None
    language = Language.objects.all()
    images = ProductImage.objects.all()
    Category = None
    
    if request.GET:   
        
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter searching keyword")
                return redirect(reverse('book'))

            queries = Q(name__icontains=query) | Q(author__icontains=query)| Q(isbn__icontains=query)| Q(publisher__icontains=query)
            books = books.filter(queries)

    context = {
        'books': books,
        'images': images,
        'language': language,
        'search': query,
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