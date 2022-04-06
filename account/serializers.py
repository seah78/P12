from rest_framework import serializers
from account.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    """
    customer serializer
    """
    class Meta:
        model = Customer
        fields = "__all__"

        
