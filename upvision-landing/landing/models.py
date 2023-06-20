from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from datetime import datetime

# Create your models here.

class ContactModel(models.Model):
    first_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=150)
    phone_number = PhoneNumberField(region='KZ')
    message = models.CharField(max_length=2000)
    date_time = models.DateTimeField(default=datetime.now)