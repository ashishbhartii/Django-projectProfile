from django.db import models
from django.utils import timezone
# We are importing timezone function from the util package of django
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone=models.CharField(max_length=10)
    filled_at = models.DateTimeField(default=timezone.now, blank=True)
    desc=models.TextField()
    id = models.AutoField(primary_key=True)
    # contact_id = models.AutoField(primary_key=True)
    # instead of objects if we want to rename bojects to an actual fields in  the admin panel
    # Django models, the __str__ method is used to define how an instance of a model should be represented as a string.
    def __str__(self):
        return self.name

class unregisteredContact(models.Model):
    name1 = models.CharField(max_length=30)
    email1 = models.EmailField()
    phone1 =models.CharField(max_length=10)
    filled_at = models.DateTimeField(default=timezone.now, blank=True)
    desc1 =models.TextField()
    id = models.AutoField(primary_key=True)
    # unregistered_id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name1

class signinData(models.Model):
    fname=models.CharField(max_length=15)
    lname=models.CharField(max_length=15)
    uname=models.CharField(max_length=15)
    email=models.EmailField()
    phone=models.CharField(max_length=10)
   
class Name(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name