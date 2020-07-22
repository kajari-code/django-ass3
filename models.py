from django.db import models

# Create your models here
class Customer(models.Model):
    Username=models.CharField(max_length=50)
    Password=models.CharField(max_length=50)
    PhoneNo=models.IntegerField()
    Address=models.CharField(max_length=50)
    