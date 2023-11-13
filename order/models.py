from django.db import models

# Create your models here


class Order(models.Model):
    order_number = models.CharField(max_length=64, null=False, editable=False)
    full