from django.db import models
from django.contrib.auth.models import User

class Resume(models.Model):
    First_Name = models.CharField(max_length=30)
    Last_Name =models.CharField(max_length=30)
    Age =models.IntegerField()
    Nationality=models.CharField(max_length=30)
    Freelance = models.CharField(max_length=30,default="Available")
    Address = models.CharField(max_length=30)
    Phone =models.IntegerField()
    Email = models.CharField(max_length=30)
    linkedin=models.CharField(max_length=30)
    languages=models.CharField(max_length=30)


class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    author = models.ForeignKey(User , on_delete=models.CASCADE)

