from django.contrib import admin
from .models import *
# Register your models here.



class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['company','address','phone','number_of_student','date_created']




class PasswordRestAdmin(admin.ModelAdmin):
    list_display = ['user','forget_password_token','date_created']


admin.site.register(Customer)
admin.site.register(Organization, OrganizationAdmin)

admin.site.register(PasswordReset ,PasswordRestAdmin)