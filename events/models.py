from django.db import models

from contract.models import Contract
from user.models import User


class Event(models.Model):
    """
    event model
    """

    STATUS_PLANNED = "planned"
    STATUS_STARTED = "started"
    STATUS_COMPLETED = "completed"
    STATUS_CHOICES = [
        (STATUS_PLANNED, "Planned"),
        (STATUS_STARTED, "Started"),
        (STATUS_COMPLETED, "Completed"),
    ]

    name = models.CharField(max_length=100, null=False)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, null=False)
    created_datetime = models.DateTimeField(auto_now_add=True)
    update_datetime = models.DateTimeField(auto_now=True)
    contract = models.ForeignKey(to=Contract, on_delete=models.DO_NOTHING)
    support_user = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)
