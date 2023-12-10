from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
# from address.models import AddressField
from django_countries.fields import CountryField
# Create your models here.

class Book_Interest(models.Model):
    """model to store customer interest in books"""
    book_name = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null= True, blank=True)

    def __str__(self):
        return self.book_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Profile(models.Model):
    """model to store customer profule information"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
    )
    full_name = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField(blank_label = "Country", null=False, blank=False, default="USA")
    email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length = 15, null=True, blank=True)
    address1 = models.CharField(max_length=64, null=True, blank=True)
    address2 = models.CharField(max_length=64, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    interest = models.ManyToManyField(Book_Interest)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

