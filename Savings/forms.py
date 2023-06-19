from django import forms
from decimal import Decimal, InvalidOperation
from .models import SavingModel

class SavingForm(forms.Form):
    currency = forms.ChoiceField(choices=SavingModel.CURRENCY_CHOICES)
    amount = forms.DecimalField(max_digits=10, decimal_places=2)

    def clean_currency(self):
        currency = self.cleaned_data.get('currency')
        if currency not in dict(SavingModel.CURRENCY_CHOICES):
            raise forms.ValidationError("Invalid currency type.")
        return currency

    def clean_amount(self):
        amount = self.cleaned_data.get('amount')
        try:
            amount = Decimal(amount)
        except InvalidOperation:
            raise forms.ValidationError("Invalid amount.")
        return amount
