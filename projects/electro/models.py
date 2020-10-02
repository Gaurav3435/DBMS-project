from django.db import models

# Create your models here.
class Products(models.Model):
 
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    category= models.CharField(max_length=30,default='Category')

