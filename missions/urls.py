from django.urls import path
from . views import  actions

app_name = 'missions'
urlpatterns = [
    path('', actions, name='mission'),
]