
from django import forms
from django.contrib.auth.models import User

from .models import *
#from products.models import Customer


    



class CustomerRegistrationForm(forms.ModelForm):

    username = forms.CharField(max_length=50, required=True, label='username',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    fullname = forms.CharField(max_length=50, required=True,label='full name',widget=forms.TextInput(attrs={'placeholder': 'full name'}))
    #last_name = forms.CharField(max_length=50, required=True,label='Last name',widget=forms.TextInput(attrs={'placeholder': 'last name'}))
    email = forms.EmailField(max_length=50, required=True,label='email',widget=forms.EmailInput(attrs={'placeholder': 'email'}))
    phone = forms.CharField(max_length=15, required=True, label='phone',widget=forms.TextInput(attrs={'placeholder': 'phone'}))
   
    password = forms.CharField(max_length=50,required=True ,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    #password2 = forms.CharField(max_length=50, required=True ,widget=forms.TextInput(attrs={'placeholder': 'Re-enter password'}))
  
    
   
    class Meta:
        model = Customer
        fields =('username','fullname' ,'phone','email','password')

    def cleaned_username(self):
        uname =self.changed_data.get('username')
        if User.objects.filter(username =uname).exists():

            # if user already exists
            raise forms.ValidationError("Customer with this username already exists")

        return uname        





class CompanyRegistrationForm(forms.ModelForm):

    username = forms.CharField(max_length=50, required=True, label='username',widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    company = forms.CharField(max_length=50, required=True,label='Organization',widget=forms.TextInput(attrs={'placeholder': "Organization's name"}))
    address = forms.CharField(max_length=50, required=True,label='Organization',widget=forms.TextInput(attrs={'placeholder': "Organization's name"}))
    number_of_student = forms.CharField(max_length=50, required=True,label='Organization',widget=forms.TextInput(attrs={'placeholder': "Organization's name"}))
  
    email = forms.EmailField(max_length=50, required=True,label='email',widget=forms.EmailInput(attrs={'placeholder': 'email'}))
    phone = forms.CharField(max_length=15, required=True, label='phone',widget=forms.TextInput(attrs={'placeholder': 'phone'}))
   
    password = forms.CharField(max_length=50,required=True ,widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
   
    
   
    class Meta:
        model = Organization
        fields =('username','company','address' ,'phone','number_of_student','email','password')

    def cleaned_username(self):
        uname =self.changed_data.get('username')
        if User.objects.filter(username =uname).exists():

            # if user already exists
            raise forms.ValidationError("Organization with this username already exists")

        return uname        
