from django.db import models

# Create your models here.
class Employee(models.Model):
    ename = models.CharField(max_length=30)
    eage = models.IntegerField()
    eemail = models.EmailField(max_length=30)
    econtact = models.IntegerField()
   

    class Meta:
        db_table = 'employee1'
