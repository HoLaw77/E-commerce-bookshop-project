from django.contrib import admin
from .models import Language, Category, Product, ProductImage
# Register your models here.

admin.site.register(Language)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)


