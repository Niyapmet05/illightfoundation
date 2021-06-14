from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
# Create your models here.



class Partner(models.Model):
    name = models.CharField(max_length=120)
    phone = PhoneField(blank=True, null=True, help_text='Contact phone number')
    phone = PhoneField(blank=True, null=True, help_text='Contact phone number')
    instagram = models.CharField(max_length=120, null=True, blank=True)
    facebook = models.CharField(max_length=120, null=True, blank=True)
    tweeter = models.CharField(max_length=120, null=True, blank=True)
    website = models.CharField(max_length=120, null=True, blank=True)
    created = models.DateTimeField(auto_now_add = True, blank=True)
    updated = models.DateTimeField(auto_now = True, blank=True)

    def __str__(self):
        return self.name

