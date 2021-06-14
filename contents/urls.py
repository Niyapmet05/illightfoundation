from django.urls import path
from . views import news

app_name = 'contents'
urlpatterns = [
    path('news/', news, name='news'),
]