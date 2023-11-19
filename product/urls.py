from django.urls import path, include
from . import views

urlpatterns = [
    path('book', views.show_book, name='book'),
    path('book_detail/<book_id>', views.book_detail, name='book_detail'),
]