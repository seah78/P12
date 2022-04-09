from rest_framework import serializers
from events.models import Event

class EventSerializer(serializers.ModelSerializer):
    """
    events serializer
    """
    class Meta:
        model = Event
        fields = '__all__'
        read_only__fields = ['created_datetime', 'update_datetime', 'contract', 'support_user', 'id']

        