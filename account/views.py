from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from account.serializers import CustomerSerializer
from account.models import Customer
from events.models import Event
from account.permissions import IsSalerContact, IsTechnicianEventContact
from user.permissions import IsManager


class CustomerViewset(ModelViewSet):

    permission_classes = [
        IsAuthenticated,
        IsSalerContact | IsTechnicianEventContact | IsManager,
    ]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    http_method_names = ["get", "post", "put"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("first_name", "email")

    def get_queryset(self):
        return Customer.objects.all()

    def list(self, request):
        if request.user.department == "seller":
            id_user = request.user.id
            customers = Customer.objects.filter(
                Q(seller=id_user) | Q(status="Prospect")
            )
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)
        elif request.user.department == "technician":
            events = Event.objects.filter(support_user=request.user.id)
            id_clients = []
            for event in events:
                id_clients.append(event.contract.customer.id)
            customer = Customer.objects.filter(id__in=id_clients)
            serializer = CustomerSerializer(customer, many=True)
            return Response(serializer.data)
        elif request.user.department == "manager":
            customer = Customer.objects.all()
            serializer = CustomerSerializer(customer, many=True)
            return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        request.data["seller"] = request.user.id
        request.POST_mutable = False
        return super(CustomerViewset, self).create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        request.POST._mutable = True
        id_client = kwargs["pk"]
        client = Customer.objects.get(id=id_client)
        request.data["seller"] = client.seller.id
        request.POST_mutable = False
        return super(CustomerViewset, self).update(request, *args, **kwargs)
