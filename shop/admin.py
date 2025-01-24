from django.contrib import admin
from shop.product import Product
from shop.category import Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)