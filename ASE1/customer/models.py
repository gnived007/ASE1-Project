from django.db import models
from django.contrib.auth.models import User


class Customer_profile(models.Model):
    Customer = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()


