from django.shortcuts import render, redirect
from .models import SavingModel, UserSaving, SharedCurrency
from .forms import SavingForm
from accounts.models import UserProfile


def savings_list(request):
    user_profile = UserProfile.objects.get(user=request.user)
    user_savings = user_profile.usersaving_set.all()

    try:
        shared_saving = SharedCurrency.objects.get(currency='WSP')
    except SharedCurrency.DoesNotExist:
        shared_saving = None

    savings = {
        'user_savings': user_savings,
        'shared_saving': shared_saving,
    }

    return render(request, 'savings/savings_list.html', savings)





def add_saving(request):
    if request.method == 'POST':
        form = SavingForm(request.POST)
        if form.is_valid():
            currency_name = form.cleaned_data['currency']
            amount = form.cleaned_data['amount']
            user_profile = UserProfile.objects.get(user=request.user)

            if currency_name == 'WSP':
                shared_currency, created = SharedCurrency.objects.get_or_create(currency='WSP')
                print(shared_currency.amount)
                shared_currency.amount += amount
                shared_currency.save()
            else:
                currency, _ = SavingModel.objects.get_or_create(currency=currency_name)

                user_saving, created = UserSaving.objects.get_or_create(
                    user_profile=user_profile,
                    currency=currency,  # pass the model instance itself
                    defaults={'amount': 0}
                )

                if not created:
                    user_saving.amount += amount
                    user_saving.save()

            return redirect("savings_list")
    else:
        form = SavingForm()

    return render(request, "savings/add_saving.html", {"form": form})











