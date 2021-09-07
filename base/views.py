from django.shortcuts import render
from rest_framework import serializers,permissions

from rest_framework.generics import ListAPIView
#from .models import StoreMasterModel
#from .serializers import StoreMasterSerializer
from .models import *
from .serializers import *
from django.db import connections
# from .permissions import IsOwner

class StoreMasterAPIView(ListAPIView):
  serializer_class=StoreMasterSerializer
  # queryset = StoreMasterModel.objects.using('sql2').raw("SELECT Sitecode , Lc_regrouping,  Area,  Sbu,  Status,  Sitecode_old,  Startdate,  Enddate,  Site_category, Site_subcategory FROM SITE_REFFERENCE")
  queryset = StoreMasterModel.objects.using('sql2').raw("EXEC SP_GENERATE_DATA '3','','',''")
  # permission_classes = (permissions.IsAuthenticated,)


class ListServerAPIView(ListAPIView):
  serializer_class=ServerListSerializer
  queryset = ServerListModel.objects.using('sql2').raw("EXEC SP_GENERATE_DATA '4','','',''")

  # def get_queryset(self):
  #     with connections['sql2'].cursor() as cursor:
  #         cursor.execute("SELECT SITECODE, SBU FROM SITE_REFFERENCE")
  #         row = cursor.fetchone()
  #         cursor.close()
  #         res_list = [x for x in row]
  #         json_rest_data = {"sitecode": res_list[0],"sbu":res_list[1] }
  #     # json = JSONRenderer().render(row)

  #     print(json_rest_data)    
  #     return json_rest_data


  # def perform_create(self, serializers):
  #     return serializers.save(owner=self.request.user)

  # def get_queryset(self):
  #     return self.queryset.filter(owner=self.request.user)

# class ExpenseDetailAPIView(RetrieveUpdateDestroyAPIView):
#   serializer_class=ExpenseSerializer
#   queryset = Expenses.objects.all()
#   permission_classes = (permissions.IsAuthenticated, IsOwner,)
#   lookup_field = 'id'


#   def perform_create(self, serializer):
#       return serializers.save(owner=self.request.user)

#   def get_queryset(self):
#       return self.queryset.filter(owner=self.request.user)




# from django.shortcuts import render
# from django.http import JsonResponse
# from rest_framework import serializers
# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# from .models import UserAccessMenu
# from .serializers import UserAccessMenuSerializer

# # Create your views here.
# @api_view(['GET'])
# def getRoutes(request):
#   routes = [
#     '/api/login/',
#   ]
#   return Response(routes)

# @api_view(['GET'])
# def getUserAccessMenu(request):
#   menu = UserAccessMenu.objects.all()
#   serializer = UserAccessMenuSerializer(menu, many=True)
#   return Response(serializer.data)  
