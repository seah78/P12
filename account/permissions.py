from rest_framework.permissions import BasePermission

from account.models import Customer
    
METHODES_CREATE_READ = [ 'GET', 'POST']
METHODES_PUT_DEL = [ 'PUT', 'DELETE']


class IsManager(BasePermission):
    def has_permission(self, request, view):
        if request.user.department == 'Manager':
            return True

class IsSalerContact(BasePermission):
    message = "L'utilisateur doit être le référent commercial du client"
    def has_permission(self, request, view): # obj
        if request.user.department == 'Seller': 
            if request.method in METHODES_PUT_DEL:
                id_customer = view.kwargs['pk']
                customer = Customer.objects.get(id=id_customer)
                if customer.seller.id == request.user.id :
                    return True
            elif request.method in METHODES_CREATE_READ:
                if not view.kwargs:
                    return True
                else:
                    id_customer = view.kwargs['pk']
                    customer = Customer.objects.get(id=id_customer)
                    if customer.seller.id == request.user.id :
                        return True
        else:
            return False

class IsTechnicianEventContact(BasePermission):
    message = "L'utilisateur doit être le gestionnaire des events du client"
    def has_permission(self, request, view):
        if request.user.department == 'Technician':
            if request.method == 'GET':
                return True
        else:
            return False