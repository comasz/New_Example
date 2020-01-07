from django.db import models

# Create your models here.
class User(models.Model):
    # these are all User objects
    Fname = models.CharField(max_length=128)
    Lname = models.CharField(max_length=128)
    Email = models.EmailField(max_length=254,unique=True)

# now go to views and add the "User" function
