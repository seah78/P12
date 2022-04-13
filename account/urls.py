from django.urls import include, path
from rest_framework import routers
from account.views import CustomerViewset

customer_router = routers.SimpleRouter(trailing_slash=False)
customer_router.register(r"client/?", CustomerViewset, basename="client")


urlpatterns = [
    path("", include(customer_router.urls)),
]
