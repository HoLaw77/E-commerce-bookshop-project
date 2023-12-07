from django.contrib import admin
from .models import Order, OrderDetail
# Register your models here.

class OrderDetailAdminInline(admin.TabularInline):
    model = OrderDetail
    readonly_fields = ('item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderDetailAdminInline,)    
    list_display = ("order_number", "full_name", 'order_total', "overall_total")
    readonly_fields = ("order_number",
    "date", )
    fields = ("order_number", "full_name", "profile", 
    "date","email", "phone_number", "address1", "address2", "postcode", 
    "countries", 'order_total', 'overall_total', 'delivery_cost')

admin.site.register(Order, OrderAdmin)

