from django.db import models
from django.db.models import Sum
import uuid
from django.conf import settings
from django_countries.fields import CountryField
from product.models import Product, ProductImage, Language, Category
from customer.models import Profile, BookInterest
# Create your models here


class Order(models.Model):
    """model to store Order with customer details"""
    order_number = models.CharField(max_length=64, null=False, editable=False)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders')
    country = CountryField(blank_label = "Country", null=False, blank=False, default="USA")
    email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length = 15, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    address1 = models.CharField(max_length=64, null=True, blank=True)
    address2 = models.CharField(max_length=64, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    order_total = models.DecimalField(max_digits=12, decimal_places=2, 
    null=False, default=0)
    delivery_cost = models.DecimalField(max_digits=12, decimal_places=2, 
    null=False, default=0)
    overall_total = models.DecimalField(max_digits=12, decimal_places=2, 
    null=False, default=0)

    def _generate_order_number(self):
        
        return uuid.uuid4().hex.upper()

    def generate_total(self):
        """Generate the total when item is added"""
        self.order_total = self.order_detail.aggregate(Sum('item_total'))['item_total__sum'] or 0
        self.delivery_cost = self.order_total * settings.DELIVERY_PERCENTAGE / 100
        self.overall_total = self.order_total + self.delivery_cost
        self.save()


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
        default = 'null'
    )
    quantity = models.IntegerField(default=0)
    item_total = models.DecimalField(max_digits=6, decimal_places=2, null=False,
    blank=False, editable=False)

    def save(self, *args, **kwargs):
        """Set it(em_total according to price * quantity"""
        self.item_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.id)