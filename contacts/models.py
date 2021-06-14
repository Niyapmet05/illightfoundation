from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField
# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1)
    birth_date = models.DateField()
    phone = PhoneField(blank=True, help_text='Contact phone number')
    phone = PhoneField(blank=True, help_text='Contact phone number')
    instagram = models.CharField(max_length=120, null=True)
    facebook = models.CharField(max_length=120, null=True)
    tweeter = models.CharField(max_length=120, null=True)
    website = models.CharField(max_length=120, null=True)
    province = models.CharField(max_length=30, null=True)
    district = models.CharField(max_length=30, null=True)
    sector = models.CharField(max_length=30, null=True)
    cell = models.CharField(max_length=30, null=True)
    village = models.CharField(max_length=30, blank=True, null=True)
    street = models.CharField(max_length=30, blank=True, null=True)
    bio = models.TextField(default='no bio...')
    function = models.CharField(max_length=30,default='Founder')
    avatar = models.ImageField(upload_to='avatar', default='no_picture.png')
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name} from {self.district} {self.sector}"

