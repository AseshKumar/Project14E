from django.db import models

class ProductModel(models.Model):
    no = models.AutoField(primary_key=True)
    name =models.CharField(max_length=50,unique=True)
    price = models.FloatField()
    quantity = models.IntegerField()
    photo = models.ImageField(upload_to="product_images/")
    pdate = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20)


class UserRegistation(models.Model):
    no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,unique=True)
    cno =models.IntegerField()
    email = models.CharField(unique=True,max_length=100)
    password = models.CharField(max_length=25)
    status = models.CharField(max_length=25)
    rdate = models.DateField(auto_now_add=True)

