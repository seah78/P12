from rest_framework.permissions import BasePermission

from account.models import Customer


class IsCustomerSellerContact(BasePermission):
    """
        Seller : can CREATE customer or prospect, can VIEW and UPDATE any prospect and their own customer, can DELETE prospect only
        Support : can VIEW their own customer
    """
    def has_permission(self, request, view):
        is_seller = request.user.department.pk == get_role_id_by_name(name="seller")
        if "pk" not in view.kwargs:
            return request.method in ["GET", "POST"] and is_seller
        customer = Customer.objects.get(pk=view.kwargs["pk"])
        return customer.seller == request.user