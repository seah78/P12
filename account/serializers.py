from rest_framework import serializers
from account.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    """
    customer serializer
    """
    class Meta:
        model = Customer
        fields = ("id", "company_name", "first_name", "last_name", "email", "phone_number", "mobile_number", "status", "seller")

        
