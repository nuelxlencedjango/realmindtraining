
from django.urls import path
from .views import *
from .import views 




app_name ="product"

urlpatterns = [
  
    path('' ,views.home,name='home'),
    path('about/' ,views.about_us,name='about'),
    path('services/' ,views.services,name='services'),
    path('blog/' ,views.blog,name='blog'),
    path('recruitment/' ,views.recruitment,name='recruitment'),
    path('contact/' ,views.contactUs,name='contact'),

     path('web/' ,views.webDevelopment,name='web'),

     path('support/' ,views.supportUs,name='support'),
     path('mobile/', views.mobileApp,name='mobile'),
    path('digital/', views.digital,name='digital'),

    path('machine/', views.machine_learning,name='machine'),
     path('game/', views.game,name='game'),
      path('database/', views.database,name='database'),

      path('train/' ,views.train,name='train'),
      path('detail/<int:pk>/', views.detail,name='detail'),
      path('product_detail/<int:pk>/', views.readmore,name='product_detail')  
]