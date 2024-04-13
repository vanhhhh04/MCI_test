from django.db import models  
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, full_name, password=None):
        if not full_name:
            raise ValueError("User must have an full name")
        user = self.model(
            full_name = full_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user 
    
    def create_superuser(self, full_name, password):
        user = self.create_user(
            full_name=full_name,
            password=password
        )
        user.is_admin=True
        user.is_active=True
        user.is_staff=True
        user.is_superadmin=True
        user.save(using=self._db)
        return user 

    def delete(self, pk):
        if self.model.is_admin == "False":
            user = self.model.delete(pk=pk)
        else :
            raise ValueError("You are not admin")

class User(AbstractBaseUser):
    # Role_Choice = (
    #     ('1', 'Admin'),
    #     ('2', 'User'),
    # )
    full_name = models.CharField(max_length=100,unique=True)
    password = models.CharField(max_length=100)
    address = models.TextField(null=True)
    school = models.CharField(max_length=100, null=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    # role = models.CharField(max_length=15, choices=Role_Choice, default='2')
    

    USERNAME_FIELD = "full_name"
    REQUIRED_FIELDS = ['password']

    objects = UserManager()


