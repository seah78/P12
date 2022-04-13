from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from events.serializers import EventSerializer
from events.permissions import IsSalerContact, IsTechnicianEventContact
from user.permissions import IsManager
from events.models import Event


class EventViewset(ModelViewSet):

    permission_classes = [
        IsAuthenticated,
        IsSalerContact | IsTechnicianEventContact | IsManager,
    ]
    serializer_class = EventSerializer
    queryset = Event.objects.all()
    http_method_names = ["get", "post", "put"]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = (
        "contract__customer__first_name",
        "contract__customer__email",
        "start_date",
    )

    def get_queryset(self):
        return Event.objects.all()

    def list(self, request):
        if request.user.department == "seller":
            events = Event.objects.filter(support_user=request.user.id)
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)
        elif request.user.department == "technician":
            events = Event.objects.filter(support_user=request.user.id)
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)
        elif request.user.department == "manager":
            events = Event.objects.all()
            serializer = EventSerializer(events, many=True)
            return Response(serializer.data)
