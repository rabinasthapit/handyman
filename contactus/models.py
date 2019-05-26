from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class ContactUs(models.Model):
    name= models.CharField(max_length=40)
    email=models.CharField(max_length=50)
    subject=models.CharField(max_length=40)
    message=RichTextField()


    def __str__(self):
        return self.name
