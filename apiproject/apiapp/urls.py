from apiapp.viewsets import Wash_UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'userdata', Wash_UserViewSet, basename='userdata')
urlpatterns = router.urls