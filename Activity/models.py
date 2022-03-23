from django.db import models

# Create your models here.
class Activity(models.Model):
    activity_name = models.CharField(max_length=200)
    activity_description = models.TextField()

    class Meta():
        db_table = "activity"