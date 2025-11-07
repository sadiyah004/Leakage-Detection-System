from django.db import models

# Create your models here.

class registertable(models.Model):
    email = models.EmailField()
    fname = models.CharField(max_length=30)
    contact_no = models.BigIntegerField()
    npassword = models.CharField(max_length=30)
    cpassword = models.CharField(max_length=30)

class feedback(models.Model):
    answer = models.CharField(max_length=200)

class profiledb(models.Model):
    uid = models.ForeignKey(registertable,on_delete=models.CASCADE,null=True)
    address = models.TextField(null=True)
    pincode = models.IntegerField(null=True)
    country = models.TextField(null=True)
    state = models.TextField(null=True)
    industry = models.TextField(null=True)
    company = models.TextField(null=True)

