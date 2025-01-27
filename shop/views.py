from django.shortcuts import render
from django.http import HttpResponse
from shop.product import Product
from shop.category import Category
from shop.forms import CustomerModelForm
from django.contrib.auth.hashers import make_password
from shop.customer import Customer

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
    # form=CustomerModelForm
    # customerform={'allcustomers':form}
    # return render(request,'signup.html',customerform)
    if request.method == "GET":
        return render(request,'signup.html')
    else:
        fn=request.POST['fn']
        ln=request.POST['ln']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=make_password(request.POST['password'])
        userdata=[fn,ln,email,mobile,password]
        print(userdata)
        
        uservalues={
            'fn':fn,
            'ln':ln,
            'email':email,
            'mobile':mobile
        }
        
        # storing the data
        customerdata=Customer(first_name=fn, last_name=ln, email=email, mobile=mobile, password=password)
        
        error_msg=None
        success_msg = None
        
        if (not fn):
            error_msg="First Name should not be empty"
        elif (not ln):
            error_msg="Last Name should not be empty"
        elif (not email):
            error_msg="Email Address should not be empty"
        elif (not mobile):
            error_msg="Mobile Number should not be empty"
        elif (not password):
            error_msg="Password should not be empty"
        elif (customerdata.isexist()):
            error_msg="Email Already Exists"
        if (not error_msg):
            success_msg="Account Created Successfully"
            customerdata.save()
            msg={'success':success_msg}
            return render(request,'signup.html',msg)
        else:
            msg={"error":error_msg,"value":uservalues}
            return render(request,'signup.html',msg)