from django.shortcuts import render
from .models import About,Quote
from contacts.models import Profile
import pandas as pd

# Create your views here.
def home(request):
    about = About.objects.all()
    quote = Quote.objects.all()
    about_df = pd.DataFrame(about).to_html()
    context = {
        'about' : about,
        'quote' : quote,

    }
    return render(request, 'hillightfoundation/home.html', context)


def about(request):
    about = Profile.objects.all()
    about_df = pd.DataFrame(about).to_html()
    context = {
        'about' : about,

    }
    return render(request, 'hillightfoundation/about.html', context)

def detail(request):
    context = {
        
    }
    return render(request, 'hillightfoundation/detail.html', context)
