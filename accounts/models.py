from django.db import models
from django.contrib.auth.models import User
# Create your models here.




class Customer(models.Model):

    user = models.OneToOneField(User,on_delete= models.SET_NULL,null=True)#,related_name='customer')
    fullname = models.CharField(max_length=200, null=True,unique=True)
 
    phone = models.CharField(max_length=11, null=True,unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
   
    
    class Meta:
        verbose_name_plural = 'Customer' 

    def __str__(self):
        return self.user.username






class Organization(models.Model):

    user = models.OneToOneField(User,on_delete= models.SET_NULL,null=True)#,related_name='customer')
    company = models.CharField(max_length=200, null=True,unique=True)
    address = models.CharField(max_length=200, null=True,unique=True)
    phone = models.CharField(max_length=11, null=True,unique=True)
    number_of_student = models.CharField(max_length=100000, null=True,unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
   
    
    class Meta:
        verbose_name_plural = 'organization' 

    def __str__(self):
        return self.user.username





class PasswordReset(models.Model):

    user = models.OneToOneField(User,on_delete= models.SET_NULL,null=True)#,related_name='customer')
    forget_password_token = models.CharField(max_length=100)
 
    #phone = models.CharField(max_length=11, null=True,unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
   
    
    class Meta:
        verbose_name_plural = 'PasswordReset' 

    def __str__(self):
        return self.user.username