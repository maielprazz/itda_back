from django.shortcuts import render
from rest_framework import serializers,permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExpenseSerializer
from .models import Expenses
from .permissions import IsOwner

# Create your views here.

class ExpenseListAPIView(ListCreateAPIView):
  serializer_class=ExpenseSerializer
  queryset = Expenses.objects.all()
  permission_classes = (permissions.IsAuthenticated,)


  def perform_create(self, serializers):
      return serializers.save(owner=self.request.user)

  def get_queryset(self):
      return self.queryset.filter(owner=self.request.user)

class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
  serializer_class=ExpenseSerializer
  queryset = Expenses.objects.all()
  permission_classes = (permissions.IsAuthenticated, IsOwner,)
  lookup_field = 'id'


  def perform_create(self, serializer):
      return serializers.save(owner=self.request.user)

  def get_queryset(self):
      return self.queryset.filter(owner=self.request.user)
