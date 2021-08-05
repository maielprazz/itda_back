from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from .models import UserAccounts

class UserAccountCreationForm(UserCreationForm):
  class Meta:
    model = UserAccounts
    fields = '__all__'