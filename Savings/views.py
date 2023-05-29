from django.shortcuts import render
from .models import SavingModel

def savings_list(request):
    savings = SavingModel.objects.all()
    return render(request, 'savings/savings_list.html', {'savings': savings})
