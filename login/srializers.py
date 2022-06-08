from rest_framework import serializers
from .models import CustomUser,UserInfo


class CustomUserSerializer(serializers.ModelSerializer):
    """
    CustomUser model serializer
    """

    class Meta:
        model = CustomUser
        fields = "__all__"

class UserInfoSerializer(serializers.ModelSerializer):
    """
    Client model serializer
    """

    class Meta:
        model = UserInfo
        fields = "__all__"
