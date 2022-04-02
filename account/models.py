from django.db import models
from user.models import User


class Customer(models.Model):
    """
    customer model
    """

    STATUS_PROSPECT = "prospect"
    STATUS_CUSTOMER = "customer"
    STATUS_CHOICES = [
        (STATUS_PROSPECT, "Prospect"),
        (STATUS_CUSTOMER, "Customer"),
    ]

    company_name = models.CharField(max_length=255, null=False)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=60, null=False, unique=True)
    phone_number = models.CharField(max_length=10)
    mobile_number = models.CharField(max_length=10)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    
    def __str__(self):
        return f"{self.company_name}"