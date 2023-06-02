from django.contrib import admin
from .models import SavingModel
# Register your models here.

class SavingsAdmin(admin.ModelAdmin):
    list_display = ["name", 'amount']
    search_fields = ['name', 'amount']

admin.site.register(SavingModel, SavingsAdmin)