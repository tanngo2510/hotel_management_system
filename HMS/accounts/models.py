from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
# Create your models here.


class Guest(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phoneNumber = PhoneNumberField(unique=True)

    def __str__(self):
        return str(self.user)

class Employee(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    phoneNumber = PhoneNumberField(unique=True)
    salary = models.FloatField()

    def __str__(self):
        return str(self.user)

