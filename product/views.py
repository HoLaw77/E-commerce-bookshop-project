from django.shortcuts import render

# Create your views here.
def show_book(request):

    return render (request, 'book/book.html')