from django.db import models

# Create your models here.
class User(models.Model):
    full_name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    address = models.TextField()
    school = models.CharField(max_length=30)