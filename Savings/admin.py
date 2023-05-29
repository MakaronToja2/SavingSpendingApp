from django.contrib import admin
from .models import SavingModel
# Register your models here.

class SavingsAdmin(admin.ModelAdmin):
    list_display = ["name", 'amount', 'category']
    search_fields = ['name', 'amount', 'category']

admin.site.register(SavingModel, SavingsAdmin)