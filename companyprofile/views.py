from django.shortcuts import render
from . models import Companyprofile
from .models import Vacancy

# Create your views here.
def company(request):
    context={
    'company':Companyprofile.objects.all(),
    'vacancy':Vacancy.objects.all(),
    }
    return render(request,'company.html',context)

def iitnepal(request):
    return render(request,'iitnepal.html')
