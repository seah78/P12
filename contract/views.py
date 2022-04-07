from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from contract.permissions import IsSalerContact
from user.permissions import IsManager
from contract.serializers import ContractSerializer
from contract.models import Contract

class ContractViewset(ModelViewSet):

    permission_classes = [IsAuthenticated, IsSalerContact | IsManager ]
    serializer_class = ContractSerializer
    queryset = Contract.objects.all()
    http_method_names = ['get', 'post', 'put']
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ("customer__first_name", "customer__last_name", 
        "customer__email", "created_datetime", "value")
    
        
    def get_queryset(self):
        return Contract.objects.all()

    def list(self, request):
        id_user = request.user.id
        contract = Contract.objects.filter(seller=id_user)
        serializer = ContractSerializer(contract, many=True)
        return Response(serializer.data)