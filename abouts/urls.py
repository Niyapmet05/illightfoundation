from django.urls import path
from . views import  home, detail, about

app_name = 'abouts'
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('<int:id>', detail, name='detail'),
]