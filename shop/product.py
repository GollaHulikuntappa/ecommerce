from django.db import models
from shop.category import Category

# Create your models here.

class Product(models.Model):
    name=models.CharField(max_length=1000)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to='img')
    desc=models.TextField()
    price=models.IntegerField()
    
    
    #static method
    @staticmethod
    def get_category_id(get_id):
        if get_id:
            return Product.objects.filter(category=get_id)
        else:
            return Product.objects.all()