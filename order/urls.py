from django.urls import path, include
from . import views

urlpatterns = [
    path('order', views.show_order, name='order'),
    path('add_order/<int:books_id>', views.add_order, name='add_order'),
    path('adjust_order/<int:books_id>', views.adjust_order, name='adjust_order'),
    path('remove_order/<int:books_id>', views.remove_order, name='remove_order'),

]