from django.shortcuts import render
from django.http import HttpResponse
from shop.product import Product
from shop.category import Category

# Create your views here.

def home(request):
    # return HttpResponse('<h1> Welcome to Ecommerce website page</h1>')
    result = Product.objects.all()
    result1= Category.objects.all()
    products= {'allproducts':result,'allcategories':result1}
    return render(request,'index.html',products)


# def displayProduct(request):
#     result = Product.objects.all()
#     products= {'allproducts':result}
#     return render(request,'product/productpage.html',products)