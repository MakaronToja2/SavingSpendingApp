from django.contrib import admin
from .models import SavingModel, SharedCurrency
# Register your models here.

class SavingsAdmin(admin.ModelAdmin):
    list_display = ["currency"]
    search_fields = ['currency']

admin.site.register(SavingModel, SavingsAdmin)

class SharedCurrencyAdmin(admin.ModelAdmin):
    list_display = ['currency', 'amount']
    search_fields = ['currency']

admin.site.register(SharedCurrency, SharedCurrencyAdmin)
