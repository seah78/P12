from rest_framework.permissions import BasePermission

from events.models import Event

METHODES_CREATE_READ = [ 'GET', 'POST']
METHODES_PUT_DEL = [ 'PUT']

class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.department == 'manager':
            if request.method == 'GET':
                return True
        else:
            return False


class IsSalerContact(BasePermission):
    message = "L'utilisateur doit être le référent commercial du contrat"

    def has_permission(self, request, view): # obj
        if request.user.department == 'seller': 
            if request.method in METHODES_CREATE_READ: #== 'POST':
                return True
        else:
            return False


class IsTechnicianEventContact(BasePermission):
    message = "L'utilisateur doit être le gestionnaire des events du contrat"

    def has_permission(self, request, view):
        if request.user.department == 'technician':
            if request.method == 'GET':
                return True
            elif request.method in ['PUT', 'DELETE']:
                id_event = view.kwargs['pk']
                event = Event.objects.get(id=id_event)
                if event.support_user.id == request.user.id :
                    return True
        else:
            return False
        

