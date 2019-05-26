from django.http import HttpResponse
from django.shortcuts import render,redirect
from slider.models import Slider
from companyprofile.models import Vacancy,Application
from blog.models import Blog
from employeeprofile.models import EmployeeProfile,CV
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from contactus.models import ContactUs
from contactus.form import ContactUsForm



# def blog(request):
#     context={
#     'blog':Blog.objects.all(),
#     }
#     return render(request,'blog-right.html',context)

def home(request):
  #databasebata object select gareko sabae leko, select * from Slider
    context= {
    'slider' :Slider.objects.all(),
    'vacancy':Vacancy.objects.all()[:2],
    }
    return render(request,'home.html',context)

    return render(request,'home.html')

def login(request):
    return render(request,'login.html')

def contactus(request):
        if request.method=='GET':
            context={
            'form':ContactUsForm(),
            }
            return render(request,'contact.html',context)
        else:
            form=ContactUsForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'contact.html',{'form':ContactUsForm(),'msg':'thankyou for your msg'})

            else:
                return render(request,'contact.html',{'form':ContactUsForm() })

def professional(request):
    context={
    'vacancy': Vacancy.objects.all(),
    }
    return render(request,'pro.html',context)

@login_required(login_url='/account/login/')
def vacancy_details(request,id):
    vacancy=Vacancy.objects.get(id=id)
    emp= EmployeeProfile.objects.get(user_id=request.user.id)
    cv=CV.objects.filter(employee_id=emp.id)
    context={
    'vacancy':vacancy,
    'cv' :cv,
    }
    return render(request,'vacancy_details.html',context)


def apply(request):
    if request.method=='POST':
        vacancy_id=request.POST.get('vacancy_id')
        cover_letter=request.POST.get('cover_letter')
        cv_id=request.POST.get('cv_id')
        vacancy=Vacancy.objects.get(id=vacancy_id)
        cv=CV.objects.get(id=cv_id)
        user=User.objects.get(id=request.user.id)
        app=Application(cv=cv,vacancy=vacancy,cover_letter=cover_letter,user=user)
        try:
            app.save()
        except:
            pass
        return redirect('home')

    else:
        return redirect('home')
