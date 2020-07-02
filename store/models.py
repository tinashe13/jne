from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=64)
    image = models.ImageField(upload_to='media')
    description = models.CharField(max_length=200)


    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=64)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products')
    image = models.ImageField(upload_to='media')
    description = models.CharField(max_length=250)


    def __str__(self):
        return self.name

