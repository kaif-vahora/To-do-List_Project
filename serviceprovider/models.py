from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class ServiceProvider(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=200)
    website = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    craeted_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'service_provider'