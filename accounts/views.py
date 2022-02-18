from django.core.mail import send_mail
from django.shortcuts import render

# Create your views here.


from django.shortcuts import render,redirect
from django.views.generic import CreateView
from django.contrib import auth, messages
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.models import Group
from .helpers import send_forgot_password_mail
from .forms import *
# Create your views here.
from .models import *
from .forms import *
import uuid

# Create your views here.
#from django.http import HttpResponse
#from django.forms import inlineformset_factory





class CustomerRegistrationView(CreateView):
    template_name = 'account/register.html'
    form_class = CustomerRegistrationForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username,email,password)

        form.instance.user = user
        
        return super().form_valid(form)





class CompanyRegistrationView(CreateView):
    template_name = 'account/organization.html'
    form_class = CompanyRegistrationForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')

        user = User.objects.create_user(username,email,password)

        form.instance.user = user
        
        return super().form_valid(form)




def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password =request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if Customer.objects.filter(user = user).exists():
                login(request,user)
                return redirect('product:home')

            elif Organization.objects.filter(user = user).exists(): 
                login(request,user)
                return redirect('product:home')   
                
            else:
                messages.info(request, 'Username OR password is incorrect')  
                 
                 

        else:
            messages.info(request, 'Username OR password is incorrect')

   
    return render(request, 'account/login.html')




def logoutPage(request):
    logout(request)
    return redirect('product:home')



def training(request):
    return render(request, 'account/training.html') 


def resetPassword(request,token):
    context = {}
    try:
        change_password = PasswordReset.objects.get(forget_password_token =token)

    except Exception as e:

        messages.success(request, 'Password changed.')

    return render(request, 'account/forget_password.html')



def forgotPassword(request):
    try:
        if request.method =='POST':
            username = request.POST.get('username')
            
            if not User.objects.filter(username=username).first(): #exists()
                messages.success(request, 'No user found with this email.')
                return redirect('accounts:reset_password')

            user_obj = User.objects.get(username=username) 
            token = str(uuid.uuid4()) 
            send_forgot_password_mail(user_obj,token)
            messages.success(request, 'A link is sent to your email.Click to reset.')


    except Exception as e:

        messages.success(request, 'A link is sent to your email.Click to reset.')

    return render(request, 'account/forgot_password.html') 