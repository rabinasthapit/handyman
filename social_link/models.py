from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class SocialLink(models.Model):
    facebook= models.CharField(max_length=20)
    instagram= models.CharField(max_length=20)
    linkedin= models.CharField(max_length=20)
    twitter= models.CharField(max_length=20)
    user= models.ForeignKey(User,default=1)

    def __str__(self):
        return self.facebook
