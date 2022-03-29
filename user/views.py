from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from user.serializers import UserSerializer
from user.models import User
from django.db.models import Q


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_names = ["get", "post", "put", "delete"]
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return User.objects.all
