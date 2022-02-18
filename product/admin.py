from django.contrib import admin

from .models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','desc']


#class PriceAdmin(admin.ModelAdmin):
 #   list_display = ['name','price', 'slug' ,'digital']


admin.site.register(Product,ProductAdmin)
admin.site.register(Course)
admin.site.register(ContactUs)