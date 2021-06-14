from django.shortcuts import render

# Create your views here.
def home(request):
    context = {

    }
    return render(request, 'hillightfoundation/home.html', context)

def detail(request):
    context = {
        
    }
    return render(request, 'hillightfoundation/home.html', context)
