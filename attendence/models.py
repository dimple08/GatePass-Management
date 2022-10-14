from django.db import models
from django.db.models.base import Model
from college.models import college 


# Create your models here.
class student(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255, default="")
    rollno=models.CharField(max_length=10, default="")
    email=models.EmailField(max_length=100, default="")
    password=models.CharField(max_length=100 , default="")
    mobile=models.IntegerField(default="")
    image=models.ImageField(default="", upload_to="upload")


class attendence(models.Model):
    attid=models.AutoField(primary_key=True)
    user=models.ForeignKey(college ,on_delete=models.CASCADE,unique=False)
    rollno=models.CharField(max_length=10, default="")
    date=models.DateField(auto_now_add=True)
    intime=models.DateTimeField(editable=False, auto_now_add=True)
    outtime=models.DateTimeField(editable=True, auto_now_add=True)

    