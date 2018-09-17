from rest_framework import serializers, viewsets
from .models import UserInfo


class UserInfoSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserInfo
        fields = ('id', 'user_name', 'user_id', 'created_at')


class ApiViewSet(viewsets.ModelViewSet):

    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerialiser
