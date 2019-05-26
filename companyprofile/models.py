from django.db import models
from django.contrib.auth.models import User
from employeeprofile.models import CV
from ckeditor.fields import RichTextField


# Create your models here.


class Companyprofile(models.Model):
    companyname= models.CharField(max_length=30)
    address = models.CharField(max_length=20)
    portfolio = models.CharField(max_length=30)
    contact = models.CharField(max_length=30)
    user= models.OneToOneField(User,default=1)

    def __str__(self):
        return self.companyname



class Vacancy(models.Model):
    title=models.CharField(max_length=20)
    description=RichTextField()
    tag= models.CharField(max_length=30)
    company=models.ForeignKey(Companyprofile,default=1)


    def __str__(self):
        return self.title

class Application(models.Model):
    vacancy = models.ForeignKey(Vacancy,on_delete=models.CASCADE)
    cv = models.ForeignKey(CV,on_delete=models.CASCADE,default=1)
    cover_letter=RichTextField(default=1)
    user=models.ForeignKey(User,default=1)


    def __str__(self):
        return str(self.cv)
