from django.shortcuts import render, redirect, reverse
from .models import Product, ProductImage, Language, Category 
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def show_book(request):

    books = Product.objects.all()
    categories = Category.objects.all()
    query = None
    language = Language.objects.all()
    images = ProductImage.objects.all()
    sort = None
    direction = None
    
    if request.GET:   
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            books = books.order_by(sortkey)
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter searching keyword")
                return redirect(reverse('book'))

            queries = Q(name__icontains=query) | Q(author__icontains=query)| Q(isbn__icontains=query)| Q(publisher__icontains=query)
            books = books.filter(queries)
            current_sort = f'{sort}_{direction}'


    context = {
        'books': books,
        'images': images,
        'current_sort': sort,
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