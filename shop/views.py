from django.shortcuts import render
from django.http import HttpResponse
from shop.product import Product
from shop.category import Category
from shop.forms import CustomerModelForm

# Create your views here.

def home(request):
    # return HttpResponse('<h1> Welcome to Ecommerce website page</h1>')
    result = Product.objects.all()
    result1= Category.objects.all()
    categoryID=request.GET.get('category')
    if categoryID:
        result = Product.get_category_id(categoryID)
    else:
        result = Product.objects.all()
    data= {'allproducts':result,'allcategories':result1}
    return render(request,'index.html',data)


# def displayProduct(request):
#     result = Product.objects.all()
#     products= {'allproducts':result}
#     return render(request,'product/productpage.html',products)


def signup(request):
    form=CustomerModelForm
    customerform={'allcustomers':form}
    return render(request,'signup.html',customerform)