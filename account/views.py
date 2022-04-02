from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from user.serializers import UserSerializer
from user.models import User
from rest_framework.response import Response


from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend

from account.serializers import CustomerSerializer
from account.models import Customer
from events.models import Event
from account.permissions import IsSalerContact, IsTechnicianEventContact, IsManager

class CustomerViewset(ModelViewSet): 

    permission_classes = [IsAuthenticated, IsSalerContact  | IsTechnicianEventContact | IsManager]
    serializer_class = CustomerSerializer
    queryset = Customer.objects.all()
    http_method_names = ['get', 'post', 'delete', 'put']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("first_name", "email")

        
    def get_queryset(self):
        print(self)
        return Customer.objects.all()

    def list(self, request):
        if request.user.role == 'Seller':
            id_user = request.user.id
            customers = Customer.objects.filter(Q(seller=id_user) | Q(status = "Prospect"))
            serializer = CustomerSerializer(customers, many=True)
            return Response(serializer.data)
        elif request.user.role == 'Technician': 
            events = Event.objects.filter(support_user=request.user.id)
            id_clients = []
            for event in events:
                id_clients.append(event.contract.customer.id)
            customer = Customer.objects.filter(id__in=id_clients)
            serializer = CustomerSerializer(customer, many=True)
            return Response(serializer.data)
        elif request.user.role == 'Manager':
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
        id_client = kwargs['pk']
        client = Customer.objects.get(id=id_client)
        request.data["seller"] = client.sales_contact.id
        request.POST_mutable = False
        return super(CustomerViewset, self).update(request, *args, **kwargs)