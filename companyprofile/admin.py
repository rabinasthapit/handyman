from django.contrib import admin

# Register your models here.
from .models import Companyprofile,Vacancy,Application
admin.site.register(Companyprofile)
admin.site.register(Vacancy)
admin.site.register(Application)
