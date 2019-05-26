from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EmployeeProfile(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    portfolio = models.URLField(max_length=30,unique=True)
    contact = models.CharField(max_length=30)
    user = models.OneToOneField(User,default=1)

    def __str__(self):
        return self.name

class Degree(models.Model):
    degreename = models.CharField(max_length=30)
    institution = models.CharField(max_length=20)
    employee = models.ForeignKey(EmployeeProfile,default=1)

    def __str__(self):
        return self.degreename


class Skill(models.Model):
    skill = models.CharField(max_length=30)
    employee = models.ForeignKey(EmployeeProfile,default=1)

    def __str__(self):
        return self.skill



class Training(models.Model):
    trainingname=models.CharField(max_length=20)
    institute=models.CharField(max_length=30)
    employee = models.ForeignKey(EmployeeProfile,default=1)

    def __str__(self):
        return self.trainingname


class Experience(models.Model):
    company= models.CharField(max_length=20)
    startdate = models.DateField(max_length=20)
    enddate = models.DateField(max_length=20)
    employee = models.ForeignKey(EmployeeProfile,default=1)



    def __str__(self):
         return self.company




class CV(models.Model):
    name= models.CharField(max_length=30)
    cv_file=models.FileField(upload_to='cv/')
    employee= models.ForeignKey(EmployeeProfile, on_delete=models.CASCADE)


    def __str__(self):
        return self.name
