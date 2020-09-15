from django.db import models

# Create your models here.
class CreateName(models.Model):
    name=models.CharField(max_length=30,unique=True,blank=False)
    def __str__(self):
        return self.name
class Question1(models.Model):
    answer1=models.CharField(max_length=20, unique=True,blank=False)
    def __str__(self):
        return self.answer1
class Question2(models.Model):
    answer2=models.CharField(max_length=20, unique=True,blank=False)
    def __str__(self):
        return self.answer2