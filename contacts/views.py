from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse

# Create your views here.
def contact(request):
    contact = Profile.objects.values
    return HttpResponse(contact)
