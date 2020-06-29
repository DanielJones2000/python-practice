from backstage.models import UserInfo
from rest_framework import serializers, viewsets


class UserInfoViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = ('id', 'displayName', 'password', 'account')


class UserInfoViewSet(viewsets.ModelViewSet):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoViewSerializer
