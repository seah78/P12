from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    user model
    """

    DEPARTMENT_MANAGER = "manager"
    DEPARTMENT_SELLER = "seller"
    DEPARTEMENT_TECHNICIAN = "technician"
    DEPARTMENT_CHOICES = [
        (DEPARTMENT_MANAGER, "Manager"),
        (DEPARTMENT_SELLER, "Seller"),
        (DEPARTEMENT_TECHNICIAN, "Technician"),
    ]

    username = models.CharField(max_length=50, null=False, unique=True)
    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField(max_length=60, null=False, unique=True)
    phone_number = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10)
    department = models.CharField(max_length=15, choices=DEPARTMENT_CHOICES)
    created_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)
