from django.contrib import admin
from shop.product import Product
from shop.category import Category
from shop.customer import Customer

class CategoryAdmin(admin.ModelAdmin):
    list_display=['name']
    
class ProductAdmin(admin.ModelAdmin):
    list_display=['name','category','image','price']
    
class CustomerAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','email','mobile','password']

# Register your models here.
admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Customer,CustomerAdmin)