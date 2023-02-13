from os import uname
from django.db import models


# Create your models here.



class user(models.Model):
           uname=models.CharField(max_length=50)
           email_id=models.EmailField(primary_key=True)
           password=models.CharField(max_length=100)
           phoneNo=models.CharField(max_length=10)

# class offerRide(models.Model):
#            emai_id=models.EmailField()
#            uname=models.CharField(max_length=50)
#            data=models.DateField()
#            leavingfrom=models.TextField()
#            goingto=models.TextField()

class offerARide(models.Model):
           email_id=models.EmailField()
           uname=models.CharField(max_length=50)
           date=models.DateField()
           leavingfrom=models.CharField(max_length=100)
           goingto=models.CharField(max_length=100)
           noOfPassenger=models.CharField(max_length=10)
           phoneNo=models.CharField(max_length=10)