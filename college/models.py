from django.db import models
from django.db.models.base import Model

# Create your models here.
class college(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=255, default="")
    rollno=models.CharField(max_length=10, default="")
    email=models.EmailField(max_length=100, default="")
    password=models.CharField(max_length=100 , default="")
    mobile=models.IntegerField(default="")
    image=models.ImageField(default="", upload_to="upload")
    