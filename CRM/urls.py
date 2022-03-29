"""CRM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from rest_framework_nested import routers
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib import admin
from django.urls import path, include

crm_router = routers.SimpleRouter(trailing_slash=False)
crm_router.register(r"/?", CRMViewSet)

urlpatterns = [
    path("", include("account.urls")),
    path("", include("contract.urls")),
    path("", include("events.urls")),
    path("", include("user.urls")),
    path('admin/', admin.site.urls),
]
