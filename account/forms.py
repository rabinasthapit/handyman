from django.forms import ModelForm
from django import forms
from employeeprofile.models import EmployeeProfile,Skill,Degree,Experience,CV
from companyprofile.models import Companyprofile,Vacancy,Application
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class RegisterForm(UserCreationForm):
    first_name=forms.CharField(max_length=100,required=True,help_text="first name")
    last_name=forms.CharField(max_length=100,required=True,help_text="last name")
    email=forms.EmailField()
    class Meta:
        model=User
        fields=('first_name','username','password1','password2','last_name','email')

class EmployeeCreateForm(ModelForm):
    class Meta:
        model=EmployeeProfile   #employeprofile bata model leko
        exclude =['user']
        # fields='__all__'




class SkillForm(ModelForm):
    class Meta:
        model= Skill
        exclude=['employee']


class DegreeForm(ModelForm):
    class Meta:
        model=Degree
        exclude=['employee']



class ExperienceForm(ModelForm):
    class Meta:
        model=Experience
        exclude=['employee']


class CVForm(ModelForm):
    class Meta:
        model=CV
        exclude=['employee']


class CompanyCreateForm(ModelForm):
    class Meta:
        model=Companyprofile
        exclude=['user']


class VacancyForm(ModelForm):
    class Meta:
        model=Vacancy
        exclude=['company']

class ApplicationForm(ModelForm):
    class Meta:
        model=Application
        fields='__all__'


class CVForm(ModelForm):
    class Meta:
        model=CV
        exclude=['employee']
