from rest_framework import serializers
from users.models import UserAccounts
from .models import UserAccessMenu

class UserAccessMenuSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserAccessMenu
    fields = '__all__' #[]
