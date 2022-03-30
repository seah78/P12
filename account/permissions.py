from rest_framework.permissions import BasePermission, SAFE_METHODS

from user.models import User
from account.models import Customer

class CustomerPermissions(BasePermission):
    """ 
    
    """
    def has_permission(self, request, view):
        if request.user.department == User.DEPARTEMENT_TECHNICIAN:
            return request.method in SAFE_METHODS
        return request.user.department == User.DEPARTMENT_SELLER
        
    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE':
            request.user.department == User.DEPARTMENT_SELLER and obj.status is False
        elif request.user.department == User.DEPARTEMENT_TECHNICIAN:
            return obj in Customer.objects.filter()
