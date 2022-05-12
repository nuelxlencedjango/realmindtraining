from multiprocessing import context
from os import name
from django.shortcuts import render,redirect ,get_object_or_404, resolve_url
from django.contrib import auth, messages
import json
import product 
from product.models import *

from django.utils import timezone


from django.http import HttpResponse,JsonResponse, request
from django.forms import inlineformset_factory
from django.views.generic.base import TemplateView

# Create your views here.

from django.views.generic import (
    ListView ,DetailView, CreateView, UpdateView ,DeleteView
)
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin ,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt


from django.db.models import Q 

from django.core.mail import send_mail

from django.conf import settings
from .forms import *






def home(request):
    product = Product.objects.all().order_by('id')
    courses = Course.objects.all().order_by('-pay')
  
    context = {
        'product':product,
        'courses':courses
    }
    return render(request, 'home.html',context)




def about_us(request):
    return render(request, 'about.html')    



def services(request):
    return render(request, 'services.html') 


def blog(request):
    return render(request, 'blog.html')     



def recruitment(request):
    return render(request, 'recruitment.html') 



def contactUs(request):
    if request.method =='POST':
        message_name = request.POST['message-name']
        message_phone = request.POST.get("message-phone" ,False)
        message_email = request.POST['message-email']
        message  = request.POST['message']

        # seend a mail
        send_mail(
            message_name , # email subject
            message ,      # main message
            message_email , # from email 
            [settings.EMAIL_HOST_USER], # recipient, to email
        fail_silently=False)
        
        
        #contacts = ContactUs(name=message_name ,phone=message_phone ,email=message_email ,message=message)
        contacts = ContactUs()
        contacts.name =message_name
        contacts.phone = message_phone
        contacts.email = message_email
        contacts.message = message
        contacts.save()


        return render(request ,'email_recieved.html',{'message_name' :message_name}) 

    else:
        return render(request ,'contact.html' ,{}) 




def webDevelopment(request):
    return render(request, 'services/web.html') 


      
def mobileApp(request):
  
    mob = Product.objects.get(name='Mobile application')
    if mob:
        context = {'mob':mob}
        return render(request, 'services/mobileapp.html',context) 

    else:
         context = {'nothing':'nothing'}
         return render(request, 'services/mobileapp.html',context) 





def detail(request, pk):
    course_detail = Course.objects.get(pk=pk)

    context={
        'course_detail':course_detail
    }

    return render(request, 'detail.html', context)




def readmore(request, pk):
    product_detail = Product.objects.get(pk=pk)

    context={
        'product_detail':product_detail
    }

    return render(request, 'readmore.html', context)    





def supportUs(request):

    return render(request, 'support.html') 



def digital(request):
    return render(request, 'digital.html')



def train(request):
    return render(request, 'train.html') 


def machine_learning(request):
    return render(request, 'machine.html')




def game(request):
    return render(request, 'game.html')




def database(request):
    return render(request, 'database.html')


    ##psycopg2==2.9.1
    #pandas==1.3.1
    ##cryptography==3.4.7
    #yarl==1.6.3