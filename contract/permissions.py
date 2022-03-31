from rest_framework.permissions import BasePermission


from contract.models import Contract


class IsContractSellerContact(BasePermission):
    """
        Seller : can CREATE new contract
                     can VIEW and UPDATE contract of their own clients if is valid
        Support : can VIEW contracts of their own clients
    """    
    def has_permission(self, request, view):
        is_seller = request.user.department.pk == get_role_id_by_name(name="seller")
        if "pk" not in view.kwargs:
            return request.method in ["GET", "POST"] and is_seller
        contract = Contract.objects.get(pk=view.kwargs["pk"])
        return contract.seller == request.user
    
