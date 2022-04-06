from django.urls import include, path
from rest_framework import routers
from events.views import EventViewset

event_router = routers.SimpleRouter(trailing_slash=False)
event_router.register(r"event/?", EventViewset, basename="event")


urlpatterns = [
    path('', include(event_router.urls)),
]