from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# from address.models import AddressField
from django_countries.fields import CountryField
# Create your models here.

class Profile(models.Model):
    """model to store customer profule information"""
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='profile'
    )
    full_name = models.CharField(max_length=100, null=True, blank=True)
    country = CountryField(blank_label = "Country", null=False, blank=False, default="USA")
    email = models.CharField(max_length=100, null=True, blank=True)
    phone_number = models.CharField(max_length = 15, null=True, blank=True)
    address1 = models.CharField(max_length=64, null=True, blank=True)
    address2 = models.CharField(max_length=64, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    

    def __str__(self):
        return self.user.username

class BookInterest(models.Model):
    """model to store customer interest in books"""
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        null=True
    )
    
    book_name = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(null= True, blank=True)

    def __str__(self):
        return self.book_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

# @receiver(post_save, sender=User)
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#         instance.profile.save()

#     def save(self, *args, **kwargs):
#         super().save(*args, **kwargs)

