from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class BlogCategory(models.Model):
    categoryname= models.CharField(max_length=30)

    def __str__(self):
        return self.categoryname

class Blog(models.Model):
    title= models.CharField(max_length=30)
    content=RichTextField()
    image=models.ImageField(upload_to='blog/')
    tag= models.CharField(max_length=30,blank=True)
    categoryname=models.ForeignKey(BlogCategory,default=1)

    def __str__(self):
        return self.title
