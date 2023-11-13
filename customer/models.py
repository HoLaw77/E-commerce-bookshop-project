from django.db import models
from django.conf import settings
from django_address import AddressField,
from django_countries import CountryField,
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    address = AddressField()
    country = CountryField()
    interest = models.ManytoManyField(Book_Interest)

class Book_Interest(model.Model):
    book_name = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null= True, blank=True)

class 