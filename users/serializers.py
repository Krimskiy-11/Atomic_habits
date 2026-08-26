from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "phone", "avatar", "first_name", "last_name", "password", "chat_id"]
