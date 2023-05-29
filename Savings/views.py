from django.shortcuts import render, redirect
from .models import SavingModel
from .forms import SavingForm

def savings_list(request):
    savings = SavingModel.objects.all()
    return render(request, 'savings/savings_list.html', {'savings': savings})

def add_saving(request):
    if request.method == "POST":
        form = SavingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('savings_list')
    else:
        form = SavingForm()

    return render(request, "savings/add_saving.html", {"form": form})

