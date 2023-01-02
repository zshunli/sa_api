from rest_framework import serializers
from .models import UserData

class Wash_UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserData
    #fields = '__all__' 呼叫所有檔案
    #可以被傳送到智慧喜的資料
    fields = ['sUserID', 'sNickName', 'sPhone', 'sAddress', 'sPictureUrl']