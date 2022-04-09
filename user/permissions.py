from rest_framework.permissions import BasePermission

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.department != 'manager':
            return False
        if request.method == 'GET':
            return True
