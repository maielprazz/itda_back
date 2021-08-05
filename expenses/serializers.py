# from django.db.models import fields
from rest_framework import serializers
from .models import Expenses

class ExpenseSerializer(serializers.ModelSerializer):
    
  class Meta:
    model=Expenses
    fields=['date', 'descriptions','amount','category']