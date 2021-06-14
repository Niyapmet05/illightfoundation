from django.shortcuts import render,redirect
from .forms import DonateForm

# Create your views here.
def donate (request):

    if request.method == 'POST':
        
        form = DonateForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = DonateForm()
        return render(request, 'hillightfoundation/donate.html', {'form': form})
    
