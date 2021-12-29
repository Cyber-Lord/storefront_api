from django.db.models import fields
from djoser.serializers import UserSerializer as BaseUserUserializer, UserCreateSerializer as BaseUserCreateSerializer

class CreateUserSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']

class UserSerializer(BaseUserUserializer):
    class Meta(BaseUserUserializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']