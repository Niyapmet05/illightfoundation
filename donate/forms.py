from django import forms
from .models import Donate

class DonateForm(forms.ModelForm):
    class Meta:
        model = Donate
        fields = ['first_name', 'last_name', 'email', 'amount',]
  