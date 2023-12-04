from django.contrib import admin
from .models import Order, OrderDetail
# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "full_name")
    readonly_fields = ("order_number", "full_name", "profile", "countries", 
    "date", "address1", "address2", "postcode", "country",)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderDetail)
