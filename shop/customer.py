from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=1000)
    last_name=models.CharField(max_length=1000)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=1000)