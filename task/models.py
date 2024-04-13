from django.db import models
from users.models import User
# Create your models here.
class Task(models.Model):
    slug = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ManyToManyField(User, blank=True)
