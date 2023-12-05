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

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderDetail(models.Model):
    """Model for OrderItem."""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_detail'
    )
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='order_detail', 
        default = ''
    )
    quantity = models.IntegerField(default=1)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False,
    blank=False, editable=False)

    def save(self, *args, **kwargs):
        """Set item_total according to price * quantity"""
        self.item_total = self.product.price * self.quantity
        super.save(*args, **kwargs)

    def __str__(self):
        return str(self.id)