from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from decimal import Decimal, InvalidOperation
from .models import SavingModel
from .forms import SavingForm

def savings_list(request):
    savings = SavingModel.objects.all()
    return render(request, 'savings/savings_list.html', {'savings': savings})

def add_saving(request):
    if request.method == 'POST':
        form = SavingForm(request.POST)
        name = request.POST.get('name')
        amount = request.POST.get('amount')
        # Validate name
        if name not in dict(SavingModel.CURRENCY_CHOICES):
            raise ValidationError("Invalid currency type.")
        # Validate and convert amount
        try:
            amount = Decimal(amount)
        except InvalidOperation:
            raise ValidationError("Invalid amount.")
        #Check if aleady exist if not create new one.
        try:
            currency = SavingModel.objects.get(name=name)
        except SavingModel.DoesNotExist:
            currency = SavingModel(name=name, amount=0)  # set initial amount to zero

        currency.amount += amount
        currency.save()

        # handle redirection or showing success message here
        return redirect("savings_list")
    else:
        form = SavingForm()

    return render(request, "savings/add_saving.html", {"form": form})

