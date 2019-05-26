from django.db import models

# Create your models here.
class Slider(models.Model):
    name =models.CharField(max_length=30)
    image= models.ImageField("upload image of 1697x650", upload_to='slider/')

    def __str__(self):
        return self.name
