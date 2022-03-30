from rest_framework import serializers
from account.models import Customer

class UserSerializer(serializers.ModelSerializer):
    """
    customer serializer
    """
    class Meta:
        model = Customer
        fields = '__all__'
        read_only__fields = ['created_datetime', 'update_datetime', 'seller', 'id']
        
