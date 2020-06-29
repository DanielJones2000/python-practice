from rest_framework import routers
from django.conf.urls import url, include
from .views.UserInfoView import UserInfoViewSet

router = routers.DefaultRouter()
router.register(r'userinfo', UserInfoViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
