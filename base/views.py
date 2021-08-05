from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import UserAccessMenu
from .serializers import UserAccessMenuSerializer

# Create your views here.
@api_view(['GET'])
def getRoutes(request):
  routes = [
    '/api/login/',
  ]
  return Response(routes)

@api_view(['GET'])
def getUserAccessMenu(request):
  menu = UserAccessMenu.objects.all()
  serializer = UserAccessMenuSerializer(menu, many=True)
  return Response(serializer.data)  

