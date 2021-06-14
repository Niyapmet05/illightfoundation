from django.shortcuts import render
from .models import Mission
import pandas as pd

# Create your views here.
def actions(request):
    action = Mission.objects.all()
    action_df = pd.DataFrame(action).to_html()
    context = {
        'action' : action,

    }
    return render(request, 'hillightfoundation/actions.html', context)

