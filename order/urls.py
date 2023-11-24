from django.urls import path, include
from . import views

urlpatterns = [
    path('order', views.show_order, name='order'),
    path('order/<product_id>/', views.add_order, name='add_order'),
]