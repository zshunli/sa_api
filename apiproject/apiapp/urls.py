from apiapp.viewsets import Wash_UserViewSet, Carbon_UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
#智慧喜
router.register(r'userdata_wash', Wash_UserViewSet, basename='userdata_wash')
#碳制郎
router.register(r'userdata_carbon', Carbon_UserViewSet, basename='userdata_carbon')


urlpatterns = router.urls
