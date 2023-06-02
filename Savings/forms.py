from django import forms
from django.db.models import Sum
from .models import SavingModel

class SavingForm(forms.Form):
    name = forms.ChoiceField(choices=SavingModel.CURRENCY_CHOICES)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)
