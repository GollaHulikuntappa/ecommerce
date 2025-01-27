from django.db import models

class Customer(models.Model):
    first_name=models.CharField(max_length=1000)
    last_name=models.CharField(max_length=1000)
    email=models.EmailField(unique=True)
    mobile=models.CharField(max_length=10)
    password=models.CharField(max_length=1000)
    
    # check if email id is exist or not
    def isexist(self):
        if Customer.objects.filter(email=self.email):
            return True
        return False
    
    # to check email id is valid or not
    @staticmethod
    def getemail(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False