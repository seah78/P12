from django.db import models
from account.models import Customer
from user.models import User


class Contract(models.Model):
    """
    contract model
    """

    STATUS_PROJECT = "project"
    STATUS_VALID = "valid"
    STATUS_CHOICES = [
        (STATUS_PROJECT, "Project"),
        (STATUS_VALID, "Valid"),
    ]

    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=False)
    value = models.FloatField()
    payment_deadline = models.DateField(null=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    seller = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
    customer = models.ForeignKey(to=Customer, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f"{self.name} - {self.customer} - "
