from rest_framework import serializers
from user.models import User

class UserSerializer(serializers.ModelSerializer):
    """
    user serializer
    """
    class Meta:
        model = User
        fields = ("id", "username", "first_name", "last_name", "email", "phone_number", "mobile_number", "department")