from django.urls import path
from . views import  home, detail

app_name = 'hillightfoundation'
urlpatterns = [
    path('', home, name='home'),
    path('<int:id>', detail, name='detail'),
]