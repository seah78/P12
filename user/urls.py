from rest_framework_simplejwt.views import TokenObtainPairView
from django.urls import path

urlpatterns = [
    path('login/', 
         TokenObtainPairView.as_view(), 
         name='obtain_tokens'),
]
