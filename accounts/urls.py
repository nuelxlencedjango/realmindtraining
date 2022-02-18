
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *
from .import views 




app_name ="accounts"

urlpatterns = [
  
   
     path('register/' ,CustomerRegistrationView.as_view(),name='register'),
      path('training/' ,views.training,name='training'),
       path('login/' ,views.loginPage,name='login'),
         path('logout/' ,views.logoutPage,name='logout'),
        path('company/' ,CompanyRegistrationView.as_view(),name='company'),   
         
         
     
          path('reset_password/' ,auth_views.PasswordResetView.as_view(),name='reset_password'),
        path('reset_password_sent/' ,auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
        path('reset/<uidb64>/<token>/' ,auth_views.PasswordResetConfirmView.as_view(template_name='account/password_reset_confirm.html'),name='password_reset_confirm'),
        path('reset_password_complete/' ,auth_views.PasswordResetCompleteView.as_view(),name='reset_password_complete'),



    
]