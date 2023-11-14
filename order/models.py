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

