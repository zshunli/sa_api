from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import UserData
from .serializers import Wash_UserSerializer, Carbon_UserSerializer

# Create your views here.
class Wash_UserViewSet(viewsets.ModelViewSet):
  queryset = UserData.objects.all()
  serializer_class = Wash_UserSerializer
  permission_classes = (AllowAny,)
  #Allowall 所有用戶、IsAuthenticated通過認證的用戶

class Carbon_UserViewSet(viewsets.ModelViewSet):
  queryset = UserData.objects.all()
  serializer_class = Carbon_UserSerializer
  permission_classes = (AllowAny,)
  #Allowall 所有用戶、IsAuthenticated通過認證的用戶