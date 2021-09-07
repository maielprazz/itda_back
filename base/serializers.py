from rest_framework import serializers
#from .models import StoreMasterModel
from .models import *

class StoreMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreMasterModel
        fields = '__all__'  
  # ['ASOFDATE' 
  # ,'SITECODE'
  # ,'COMPCODE'   
  # ,'STOREDESC' 
  # ,'MALLNAME' 
  # ,'TELP' 
  # ,'EMAIL' 
  # ,'CONCEPT' 
  # ,'PROVINCE' 
  # ,'REGION' 
  # ,'GM_OM' 
  # ,'GM_MAIL' 
  # ,'OM_NAME' 
  # ,'OM_MAIL' 
  # ,'OM_PHONE' 
  # ,'OIC_NAME' 
  # ,'OIC_MAIL' 
  # ,'OIC_PHONE' 
  # ,'SBU'   
  # ,'STORETYPE' 
  # ,'SITEPROFILE'] 
  
class ServerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerListModel
        fields = '__all__'  

# from rest_framework import serializers
# from users.models import UserAccounts
# from .models import UserAccessMenu

# class UserAccessMenuSerializer(serializers.ModelSerializer):
#   class Meta:
#     model = UserAccessMenu
#     fields = '__all__' #[]
