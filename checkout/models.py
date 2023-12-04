from django.db import models
import uuid
from django_countries.fields import CountryField
from product.models import Product, ProductImage, Language, Category
from customer.models import Profile, Book_Interest
# Create your models here


class Order(models.Model):
    """model to store Order with customer details"""
    order_number = models.CharField(max_length=64, null=False, editable=False)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders')
    countries = CountryField()
    date = models.DateTimeField(auto_now_add=True)
    address1 = models.CharField(max_length=64, null=True, blank=True)
    address2 = models.CharField(max_length=64, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=70, null=True, blank=True)

    def _generate_order_number(self):
        
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.order_full_name

class OrderDetail(models.Model):
    """Model for OrderItem."""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_detail'
    )
    
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)