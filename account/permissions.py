from rest_framework.permissions import BasePermission

from user.models import User
from account.models import Customer

class CustomerPermissions(BasePermission):
    pass