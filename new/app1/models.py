from django.db import models
from django.contrib.auth.models import AbstractUser

class app1(models.Model):   #TABLE DEFINITION
    cover=models.ImageField(upload_to='app1/img',null=True,blank=True)
    name=models.CharField(max_length=30)
    description=models.CharField(max_length=100)


    def __str__(self):
        return self.name

# Create your models here.
class team(models.Model):
    image=models.ImageField(upload_to='app1/img',null=True,blank=True)
    name=models.CharField(max_length=30)
    about=models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Myuser(AbstractUser):
    place=models.CharField(max_length=20)
    phone=models.CharField(max_length=20)

