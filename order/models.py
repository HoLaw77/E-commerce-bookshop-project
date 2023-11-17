from django.db import models
from django.address import AddressField
from django.countries import CountryField
# Create your models here


class Order(models.Model):
    """model to store Order with customer details"""
    order_number = models.CharField(max_length=64, null=False, editable=False)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    address = AddressField()
    countries = CountryField()
    date = models.DateTimeField(auto_now_add=True)

    def _generate_order_number(self):
        
        return uuid.uuid4().hex.upper()

    def __str__(self):
        return self.order_number

class OrderDetail(models.Model):
    """Model for OrderItem."""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_detail'
    )
    product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.CASCADE,
        related_name='order_item_inventory'
    )
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)