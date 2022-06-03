from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.urls import reverse
User = get_user_model()


from cloudinary.models import CloudinaryField






class Product(models.Model):
   name=models.CharField(max_length=200)
   desc=models.TextField()
   #img = CloudinaryField(blank=True,null=True)
   icon = models.CharField(max_length=100,unique=False, default =None,blank=True,null=True)
   
   
   class Meta:
      verbose_name_plural='Products'

   def get_absolute_url(self):
        return reverse('product:detail', args[self.id])

   def __str__(self):
      return self.name    

    

class Course(models.Model):
   name=models.CharField(max_length=200)
   desc=models.TextField()
   img = CloudinaryField(blank=True,null=True)
   pay = models.FloatField(default=0)
   #icon = models.CharField(max_length=100,unique=False, default =None,blank=True,null=True)
   

   def get_absolute_url(self):
        return reverse('product:product_detail', args[self.id])


   class Meta:
      verbose_name_plural='courses'

   def __str__(self):
      return self.name    





class ContactUs(models.Model):

   name = models.CharField(max_length=100) 
   email = models.EmailField(unique = False) 
   phone = models.CharField(max_length=20) 
   message = models.TextField(max_length=100)


   class Meta:
      verbose_name_plural = "Contact Us"

   def __str__(self):
      return self.name        





