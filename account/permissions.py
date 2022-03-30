from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
from django.core.exceptions import ObjectDoesNotExist

from account.models import Customer