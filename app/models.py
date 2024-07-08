# myapp/models.py
from django.db import models
import uuid

class User(models.Model):
    userId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    firstName = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100, null=False)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=100, null=False)
    phone = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.email

class Organisation(models.Model):
    orgId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
