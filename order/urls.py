from django.urls import path, include
from . import views

urlpatterns = [
    path('order', views.show_order, name='order'),
]