from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mission(models.Model):  
    contributor = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    mission = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.mission

