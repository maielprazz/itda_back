from django.db.models.fields.related import OneToOneField
from users.models import UserAccounts
from django.db import models
# from django.contrib.auth.models import UserAccounts

# Create your models here.
# class UserAccessMenu(models.Model):
#   useraccessid = models.AutoField(primary_key=True, editable=False)
#   accountname = models.OneToOneField(UserAccounts,on_delete=models.CASCADE, null=False)
#   email = models.EmailField(blank=False, unique=True)
#   created_at = models.DateTimeField(auto_now_add=True)
#   updated_at = models.DateTimeField(auto_now=True)
#   grpMenuA = models.BooleanField(default=False)
#   grpMenuA1 = models.BooleanField(default=False)
#   grpMenuA2 = models.BooleanField(default=False)
#   grpMenuA3 = models.BooleanField(default=False)
#   grpMenuA4 = models.BooleanField(default=False)
#   grpMenuA5 = models.BooleanField(default=False)
#   grpMenuA6 = models.BooleanField(default=False)
#   grpMenuA7 = models.BooleanField(default=False)
  
#   def __str__(self):
#     return f'Menu Access for ' + str(self.accountname)
