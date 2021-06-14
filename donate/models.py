from django.db import models

# Create your models here.
class Donate(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField()
    amount = models.FloatField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} with {self.email} gives {self.amount}'
