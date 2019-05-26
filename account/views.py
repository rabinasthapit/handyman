from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import RegisterForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login
from employeeprofile.models import EmployeeProfile,Skill,Degree,Experience,CV
from .forms import EmployeeCreateForm,SkillForm,DegreeForm,ExperienceForm,CVForm
from companyprofile.models import Companyprofile,Vacancy,Application
from .forms import CompanyCreateForm,VacancyForm,ApplicationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='GET':
        context={
        'form':RegisterForm(),
        }
        return render(request,'register.html',context)
    else:
        form=RegisterForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                username= request.POST.get('username')
                password = request.POST.get('password1')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request,user)

                return redirect('whoareyou')

            except:
                return render(request,'register.html', {'form':form})

        else:
            context={
            'form':form,
            }

            return render(request,'register.html',context)
        # context={}
        # e= request.POST.get('email')
        # p1= request.POST.get('password1')
        # p2=request.POST.get('password2')
        # if p1==p2:
        #     u= User(username=e,email=e,password=p1) #u object banako and constructor initialized
        #     try:
        #         u.save()
        #         context.update({'msg':'Successfully Account created'}) #dictionary
        #     except:
        #         context.update({'errmsg':'Some error occured or your email may already used' })
        #     return render(request,'register.html',context)
        # else:
        #     context.update({'errmsg': 'Password doesnot match'})
        #     return render (request,'register.html',context



#user_update_info
@login_required(login_url='account/login/')
def user_update(request):
    emp= EmployeeProfile.objects.get(user_id=request.user.id)
    form= EmployeeCreateForm(request.POST or None,instance=emp)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context={
    'form':form,
        }
    return render(request,'user_update.html',context)

#user_skill
@login_required(login_url='account/login/') #decorators
def user_skill(request):
    if request.method=='GET':
        emp = EmployeeProfile.objects.get(user_id=request.user.id)
        skill=Skill.objects.filter(employee_id=emp.id)
        context={
        'skill' : skill,
        'form' : SkillForm(),
        }
        return render(request,'user_skill.html', context)

    else:
        form=SkillForm(request.POST)
        if form.is_valid():
            sk=form.save(commit=False)
            emp = EmployeeProfile.objects.get(user_id=request.user.id)
            sk.employee=emp
            sk.save()
            return redirect('user_skill')

        else:
            emp = EmployeeProfile.objects.get(user_id=request.user.id)
            skill=Skill.objects.filter(employee_id=emp.id)
            context={
            'skill' : skill,
            'form' : SkillForm(),
            }
            return render(request,'user_skill.html', context)


#user_skill_delete
@login_required(login_url='account/login/') #decorators
def user_skill_delete(request,id):
    try:
        skill=Skill.objects.get(id=id)
        skill.delete()
        return redirect('user_skill')

    except:
        return redirect('user_skill')

#cv form
@login_required(login_url='account/login/') #decorators
def user_cv(request):
    if request.method=='GET':
        emp=EmployeeProfile.objects.get(user_id=request.user.id)
        context={
        'form':CVForm(),
        'cv':CV.objects.filter(employee_id=emp.id)
        }
        return render(request,'user_cv.html',context)
    else:
        form=CVForm(request.POST,request.FILES)
        if form.is_valid():
            cv_data=form.save(commit=False)
            emp=EmployeeProfile.objects.get(user_id=request.user.id)
            cv_data.employee=emp
            cv_data.save()
            return redirect('user_cv')

        else:
            return redirect('user_cv')

#cv UPDATE
@login_required(login_url='account/login/') #decorators
def user_cv_update(request,id):
    cv=CV.objects.get(id=id)
    form=CVForm(request.POST or None,request.FILES or None ,instance=cv)
    if form.is_valid():
        form.save()
        return redirect('dashboard')
    context={
    'form': form
    }

    return render(request,'cv_update.html',context)


#user_cv_delete
@login_required(login_url='account/login/') #decorators
def user_cv_delete(request,id):
    try:
        cv=CV.objects.get(id=id)
        cv.delete()
        return redirect('user_cv')

    except:
        return redirect('user_cv')

#user_degree_add

@login_required(login_url='account/login/')
def user_degree(request):
    if request.method=='GET':
        emp = EmployeeProfile.objects.get(user_id=request.user.id)
        degree=Degree.objects.filter(employee_id=emp.id)
        context={
        'degree' : degree,
        'form' : DegreeForm(),
        }
        return render(request,'user_degree.html', context)

    else:
        form=DegreeForm(request.POST)
        if form.is_valid():
            dg=form.save(commit=False)
            emp = EmployeeProfile.objects.get(user_id=request.user.id)
            dg.employee=emp
            dg.save()
            return redirect('user_degree')

        else:
            emp = EmployeeProfile.objects.get(user_id=request.user.id)
            degree=Degree.objects.filter(employee_id=emp.id)
            context={
            'degree' : degree,
            'form' : DegreeForm(),
            }
            return render(request,'user_degree.html', context)

#user_degree_delete
@login_required(login_url='account/login/') #decorators
def user_degree_delete(request,id):
    try:
        degree=Degree.objects.get(id=id)
        degree.delete()
        return redirect('user_degree')

    except:
        return redirect('user_degree')

#user_experience
@login_required(login_url='account/login/')
def user_experience(request):
    if request.method=='GET':
        emp = EmployeeProfile.objects.get(user_id=request.user.id)
        experience=Experience.objects.filter(employee_id=emp.id)
        context={
        'experience' : experience,
        'form' : ExperienceForm(),
        }
        return render(request,'user_experience.html', context)

    else:
        form=ExperienceForm(request.POST)
        if form.is_valid():
            exp=form.save(commit=False)
            emp = EmployeeProfile.objects.get(user_id=request.user.id)
            exp.employee=emp
            exp.save()
            return redirect('user_experience')

        else:
            emp = EmployeeProfile.objects.get(user_id=request.user.id)
            experience=Experience.objects.filter(employee_id=emp.id)
            context={
            'experience' : experience,
            'form' : ExperienceForm(),
            }
            return render(request,'user_experience.html', context)

#user_experience_delete
@login_required(login_url='account/login/') #decorators
def user_experience_delete(request,id):
    try:
        experience=Experience.objects.get(id=id)
        experience.delete()
        return redirect('user_experience')

    except:
        return redirect('user_experience')

#add_vacancy_company
@login_required(login_url='account/login/') #decorators
def add_vacancy(request):
    if request.method=='GET':
        context={
        'form':VacancyForm,
        }
        return render(request,'add_vacancy.html',context)
    else:
        form=VacancyForm(request.POST)
        if form.is_valid():
            vacancy=form.save(commit=False)
            company=Companyprofile.objects.get(user_id=request.user.id)
            vacancy.company=company
            vacancy.save()
            return redirect('companydashboard')

        else:
            return render(request,'add_vacancy.html',{'form':form })

#list_all_vacancy
@login_required(login_url='account/login/')
def list_vacancy(request):
    company=Companyprofile.objects.get(user_id=request.user.id)
    vacancy=Vacancy.objects.filter(company_id=company.id)
    return render(request,'list_vacancy.html',{'vacancy':vacancy})

#update_vacancy

@login_required(login_url='account/login/') #decorators
def update_vacancy(request,id):
    vacancy=Vacancy.objects.get(id=id)
    form=VacancyForm(request.POST or None,request.FILES or None ,instance=vacancy)
    if form.is_valid():
        form.save()
        return redirect('companydashboard')
    context={
    'form': form
    }

    return render(request,'update_vacancy.html',context)



#delete vacancy
@login_required(login_url='account/login/') #decorators
def delete_vacancy(request,id):
    try:
        vacancy=Vacancy.objects.get(id=id)
        vacancy.delete()
        return redirect('list_vacancy')

    except:
        return redirect('list_vacancy')


#read_more vacancy
@login_required(login_url='account/login/')
def readmore_vacancy(request,id):
    context={}
    try:
        context.update({'readmore':Vacancy.objects.get(id=id)})
        return render(request,'readmore.html',context)
    except:
        return render(request,'404.html')



def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')

    else:
        return redirect('login')



def whoareyou(request):
    if request.user.is_authenticated():             #securing the page
        login_user_id=request.user.id
        try:
            u=EmployeeProfile.objects.get(user_id=login_user_id)
            return redirect('dashboard')
        except:
            try:
                u=Companyprofile.objects.get(user_id=login_user_id)
                return redirect('companydashboard')
            except:
                return render(request,'whoareyou.html')
    else:
        return redirect('login')



def employee(request):
    if request.user.is_authenticated():
        if request.method=='GET':
            context={
            'form':EmployeeCreateForm(),
            }
            login_user_id=request.user.id
            try:
                u=EmployeeProfile.objects.get(user_id=login_user_id)
                return redirect('skill')
            except:
                return render(request,'employee_create.html',context)
        else:
            form=EmployeeCreateForm(request.POST)
            if form.is_valid():
                employee_data=form.save(commit=False)  #saves in emplyeedata instead of database
                login_user_id = request.user.id    #takes out the id of currently logged user
                login_user=User.objects.get(id=login_user_id)   #SELECT * from 'user' where id=30'
                employee_data.user= login_user
                try:
                    employee_data.save()
                    return redirect('skill')
                except:
                    return render(request,'employee_create.html',{'form':form,'msg':'with this user account is already created'} )
            else:
                return render(request,'employee_create.html',{'form':form})



def skill(request):
    if request.user.is_authenticated():
        if request.method=='GET':
            context={
            'form':SkillForm()
            }
            login_user_id=request.user.id
            emp=EmployeeProfile.objects.get(user_id=login_user_id)
            try:
                skill=Skill.objects.get(employee_id=emp.id)
                return redirect('degree')
            except:
                return render(request,'skill.html',context)
        else:
            form=SkillForm(request.POST)
            if form.is_valid():
                skill=form.save(commit=False)
                login_user_id=request.user.id
                emp=EmployeeProfile.objects.get(user_id=login_user_id)
                skill.employee=emp
                try:
                    skill.save()
                    return redirect('degree')
                except:
                    return render(request,'skill.html',{'form':form,'msg':'you have already inserted the skill'})

            else:
                return render(request,'skill.html',context)
    else:
        return redirect('login')




def degree(request):
    if request.user.is_authenticated():
        if request.method=='GET':
            context={
            'form':DegreeForm()

            }
            login_user_id=request.user.id
            emp=EmployeeProfile.objects.get(user_id=login_user_id)
            try:
                degree=Degree.objects.get(employee_id=emp.id)
                return redirect('experience')
            except:
                return render(request,'degree.html',context)
        else:
            form=DegreeForm(request.POST)
            if form.is_valid():
                degree=form.save(commit=False)
                login_user_id=request.user.id
                emp=EmployeeProfile.objects.get(user_id=login_user_id)
                degree.employee=emp
                try:
                    degree.save()
                    return redirect('experience')
                except:
                    return render(request,'degree.html',{'form':form,'msg':'you have already inserted the degree'})

            else:
                return render(request,'degree.html')
    else:
        return redirect('login')



def experience(request):
    if request.user.is_authenticated():
        if request.method=='GET':
            context={
            'form':ExperienceForm()

            }
            login_user_id=request.user.id
            emp=EmployeeProfile.objects.get(user_id=login_user_id)
            try:
                experience=Experience.objects.get(employee_id=emp.id)
                return redirect('cv')
            except:
                return render(request,'experience.html',context)
        else:
            form=ExperienceForm(request.POST)
            if form.is_valid():
                experience=form.save(commit=False)
                login_user_id=request.user.id
                emp=EmployeeProfile.objects.get(user_id=login_user_id)
                experience.employee=emp
                try:
                    experience.save()
                    return redirect('dashboard')
                except:
                    return render(request,'experience.html',{'form':form,'msg':'you have already inserted the experience'})

            else:
                return render(request,'experience.html',context)
    else:
        return redirect('login')

def cv(request):
    if request.user.is_authenticated():
        if request.method=='GET':
            context={
            'form':CVForm()

            }
            login_user_id=request.user.id
            emp=EmployeeProfile.objects.get(user_id=login_user_id)
            try:
                cv=CV.objects.get(employee_id=emp.id)
                return redirect('dashboard')
            except:
                return render(request,'cv.html',context)
        else:
            form=CVForm(request.POST,request.FILES)
            if form.is_valid():
                cv=form.save(commit=False)
                login_user_id=request.user.id
                emp=EmployeeProfile.objects.get(user_id=login_user_id)
                cv.employee=emp
                try:
                    cv.save()
                    return redirect('dashboard')
                except:
                    return render(request,'cv.html',{'form':form,'msg':'you have already inserted the file'})

            else:
                return render(request,'cv.html',context)
    else:
        return redirect('login')


def company(request):
    if request.user.is_authenticated():
        if request.method=='GET':
            context={
            'form':CompanyCreateForm(),
            }
            login_user_id=request.user.id
            try:
                u=Companyprofile.objects.get(user_id=login_user_id)
                return redirect('companydashboard')
            except:
                return render(request,'company_create.html',context)
        else:
            form=CompanyCreateForm(request.POST)
            if form.is_valid():
                company_data=form.save(commit=False)  #saves in companydata instead of database
                login_user_id = request.user.id    #takes out the id of currently logged user
                login_company=User.objects.get(id=login_user_id)   #SELECT * from 'user' where id=30'
                company_data.user= login_company
                try:
                    company_data.save()
                    return redirect('vacancy')
                except:
                    return render(request,'company_create.html',{'form':form,'msg':'invalid '} )
            else:
                return render(request,'company_create.html',{'form':form})

def companydashboard(request):
    if request.user.is_authenticated:
        return render(request,'companydashboard.html')

    else:
        return redirect('login')


def vacancy(request):
    if request.user.is_authenticated():
        if request.method=='GET':
            context={
            'form':VacancyForm(),
            }
            return render(request,'vacancy.html',context)
        else:
            form=VacancyForm(request.POST)
            if form.is_valid():
                company_data=form.save(commit=False)  #saves in emplyeedata instead of database
                login_user_id = request.user.id    #takes out the id of currently logged user
                login_company=Companyprofile.objects.get(user_id=login_user_id)   #SELECT * from 'user' where id=30'
                company_data.company= login_company
                company_data.save()
                return redirect('companydashboard')
            else:
                return render(request,'vacancy.html',{'form':form})
    else:
        return redirect('login')
def application(request):
    if request.user.is_authenticated():
        if request.method=='GET':
            context={
            'form':ApplicationForm(),
            }
            login_user_id=request.user.id
            try:
                u=Companyprofile.objects.get(user_id=login_user_id)
                return redirect('dashboard')
            except:
                return render(request,'application.html',context)
        else:
            form=ApplicationForm(request.POST)
            if form.is_valid():
                company_data=form.save(commit=False)  #saves in emplyeedata instead of database
                login_user_id = request.user.id    #takes out the id of currently logged user
                login_user=User.objects.get(id=login_user_id)   #SELECT * from 'user' where id=30'
                company_data.user= login_user
                try:
                    company_data.save()
                    return redirect('dashboard')
                except:
                    return render(request,'application.html',{'form':form,'msg':'already exists'} )
            else:
                return render(request,'application.html',{'form':form})
