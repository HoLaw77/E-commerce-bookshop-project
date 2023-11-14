from django.db import models
from django.conf import settings
from django_address import AddressField,
from django_countries import CountryField,
# Create your models here.


class Profile(models.Model):
    """model to store customer profule information"""
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    address = AddressField()
    country = CountryField()
    interest = models.ManytoManyField(Book_Interest)

    def __str__(self):
        return self.first_name 

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

class Book_Interest(model.Model):
    """model to store customer interest in books"""
    book_name = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null= True, blank=True)

    def __str__(self):
        return self.book_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)