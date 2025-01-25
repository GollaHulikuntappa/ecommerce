from django.contrib import admin
from shop.product import Product
from shop.category import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','category','image','price']

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)