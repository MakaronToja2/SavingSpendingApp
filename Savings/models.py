from django.db import models
from django.contrib.auth.models import User
from accounts.models import UserProfile

class SavingModel(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'Dollar'),
        ('EUR', 'Euro'),
        ('PLN', 'Polish Zloty'),
        ('WSP', 'Wspolne'),
    ]

    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, unique=True)


    def __str__(self):
        return self.get_currency_display()  # returns the verbose name of the currency


class SharedCurrency(models.Model):
    CURRENCY_CHOICES = [
        ('WSP', 'Wspolne'),
    ]

    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)


class UserSaving(models.Model):
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    currency = models.ForeignKey(SavingModel, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f"{self.user_profile.user.username}'s {self.currency}"

