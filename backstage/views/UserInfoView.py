from rest_framework import routers, serializers, viewsets
from backstage.models import UserInfo

class UserInfoViewSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
        model = UserInfo
        fields = ['id', 'displayName', 'password', 'account']

class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoViewSerializer
    
router = routers.DefaultRouter()
router.register(r'userinfo', UserInfoViewSet)