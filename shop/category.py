from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.name