from django.urls import include, path
from rest_framework import routers
from contract.views import ContractViewset

contract_router = routers.SimpleRouter(trailing_slash=False)
contract_router.register(r"contract/?", ContractViewset, basename="contract")


urlpatterns = [
    path('', include(contract_router.urls)),
]