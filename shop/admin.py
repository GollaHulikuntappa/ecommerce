from django.contrib import admin
from shop.product import Product
from shop.category import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']

# Register your models here.
admin.site.register(Product)
admin.site.register(Category,CategoryAdmin)