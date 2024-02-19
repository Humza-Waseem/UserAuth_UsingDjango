from django.db import models
from django.contrib.auth.models import AbstractUser



# Create your models here.

class User(AbstractUser):
    name  = models.CharField(max_length=75,unique = True, null= True)
    email = models.EmailField(max_length=150,unique = True)
    dp = models.ImageField(default='default.jpg')
    
    USERNAME_FIELD = 'email' # HERE WE CHANGED THE USERNAME FIELD TO EMAIL, WHICH IS REQUIRED FOR LOGIN at ADMIN PANEL
    REQUIRED_FIELDS = []