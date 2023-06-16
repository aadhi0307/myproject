from django.db import models

# Create your models here.
class userdb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    mobile = models.IntegerField(null=True, blank=True)
    image=models.ImageField(upload_to="profile",null=True,blank=True)
    pwd=models.CharField(max_length=50, null=True, blank=True)
    cpwd=models.CharField(max_length=50, null=True, blank=True)

class contactdb(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    subject = models.CharField(max_length=50, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)

class cartdb(models.Model):
    username=models.CharField(max_length=100, null=True, blank=True)
    pname=models.CharField(max_length=100, null=True, blank=True)
    description=models.CharField(max_length=200, null=True, blank=True)
    quantity=models.IntegerField( null=True, blank=True)
    price=models.IntegerField( null=True, blank=True)


