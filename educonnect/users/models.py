from django.db import models
from django.contrib.auth.models import User

import uuid

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    username = models.CharField(max_length=350)
    firstname = models.CharField(max_length=350)
    lastname = models.CharField(max_length=350)
    phonenumber = models.CharField(max_length=11)
    email = models.EmailField(max_length=350)
    role = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    created = models.DateField(auto_now_add=True)
    
    def __str__(self) -> str:
        return str(self.user.username)