from django.urls import path
from . views import donate

app_name = 'donates'
urlpatterns = [
    path('', donate, name='donate'),
]