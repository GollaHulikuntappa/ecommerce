from django.urls import path
from shop import views

urlpatterns = [
    path('',views.home),
    path('signup/',views.signup),
    # path('productpage/',views.displayProduct)
]
