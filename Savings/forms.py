from django import forms
from .models import SavingModel

class SavingForm(forms.ModelForm):
    class Meta:
        model = SavingModel
        fields = ["name", "amount", "category"]