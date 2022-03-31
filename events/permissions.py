from rest_framework.permissions import BasePermission


from events.models import Event

class IsEventSupportContact(BasePermission):
    """
        Seller : can CREATE new event, can VIEW events of their own customer, can UPDATE events of their own customer if not completed
        Support : can VIEW events of their own customer
                       can UPDATE events of their own customer if not completed 
    """
    def has_permission(self, request, view):
        is_support = request.user.department.pk == get_role_id_by_name(name="technician")
        if "pk" not in view.kwargs:
            return request.method in ["GET", "POST"] and is_support
        event = Event.objects.get(pk=view.kwargs["pk"])
        return event.support_user == request.user