from django.db import models

# Create your models here.
class categorydb(models.Model):
    cname=models.CharField(max_length=50,null=True,blank=True)
    image=models.ImageField(upload_to="category",null=True,blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)

class productdb(models.Model):
    category=models.CharField(max_length=50,null=True,blank=True)
    pname=models.CharField(max_length=50,null=True,blank=True)
    price=models.IntegerField(null=True,blank=True)
    brand=models.CharField(max_length=50,null=True,blank=True)
    pimage=models.ImageField(upload_to="product",null=True,blank=True)
    description = models.CharField(max_length=50, null=True, blank=True)


