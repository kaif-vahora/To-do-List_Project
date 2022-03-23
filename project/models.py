from turtle import update
from unicodedata import category
from django import db
from django.db import models

# Create your models here.
#we have extended models class here to use models class variable
class project(models.Model):
    project_name =models.CharField(max_length=30)
    project_description =models.TextField()
    project_complition =models.DateTimeField()
    project_color =models.CharField(max_length=30,null=True)
    project_status =models.BooleanField(default=True,null=True)
    created_at =models.DateTimeField(auto_now_add=True,null=True)
    update_at =models.DateTimeField(auto_created=True,null=True)

class projectCategory(models.Model):
    category_name =models.CharField(max_length=30)
    category_description = models.TextField()
    class Meta:
        db_table = 'project_category'
