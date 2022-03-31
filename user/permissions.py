from rest_framework.permissions import BasePermission


from user.models import User

class IsManager(BasePermission):
    """
        Manager : Read only on the CRM
    """
    def has_permission(self, request, view):
        return request.user.department.value == "manager"


