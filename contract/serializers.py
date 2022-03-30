from rest_framework import serializers
from contract.models import Contract

class UserSerializer(serializers.ModelSerializer):
    """
    contract serializer
    """
    class Meta:
        model = Contract
        fields = '__all__'
        read_only__fields = ['created_datetime', 'update_datetime', 'seller', 'customer', 'id']
        
        