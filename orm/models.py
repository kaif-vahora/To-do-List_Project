from sre_constants import CATEGORY
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Role(models.Model):
    role_name = models.CharField(max_length=30)
    role_description = models.TextField()
    class Meta:
        db_table = 'role'

class Employee(Role):
    employyee_name = models.CharField(max_length=30)
    employyee_email = models.CharField(max_length=30)
    employyee_password = models.CharField(max_length=30)
    employyee_phone = models.CharField(max_length=30)
    employyee_address = models.TextField(max_length=30)
    employyee_dob = models.DateField(max_length=30)
    class Meta:
        db_table = 'employee'

# one to one relationship
class Student(models.Model):
    #role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    role_id = models.OneToOneField(Role, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=30)
    student_email = models.CharField(max_length=30)
    student_password = models.CharField(max_length=30)
    student_phone = models.CharField(max_length=30)
    student_address = models.TextField(max_length=30)
    student_dob = models.DateField(max_length=30)
    class Meta:
        db_table = 'student'        

class Customer(models.Model):
    customer_name = models.CharField(max_length=30)
    class Meta:
        db_table = 'customer'        

class Product(models.Model):
    CATEGORY = (('indor','indor'),('outdoor','outdoor'))
    name = models.CharField(max_length=200)
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'product'

class Order(models.Model):
    STATUS = (('pending','pending'),('od','od'),('delivered','delivered'))
    customer = models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200,choices=STATUS)
    class Meta:
        db_table = 'order'