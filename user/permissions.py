from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist

from user.models import User

class IsManager(BasePermission):
    def is_manager(self, user):
        pass
        
        """
        try:
            User.objects.get(user=user  )
        """
            
            
            
class IsSeller(BasePermission):
    def is_saler(self, user):
        pass
        
        
class IsSupport(BasePermission):
    def is_support(self, user):
        pass