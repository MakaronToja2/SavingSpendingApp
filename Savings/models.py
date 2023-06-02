from django.db import models

# Create your models here.
class SavingModel(models.Model):
    CURRENCY_CHOICES = [
        ('USD', 'Dollar'),
        ('EUR', 'Euro'),
        ('PLN', 'Polish Zloty'),
    ]

    name = models.CharField(max_length=3, choices=CURRENCY_CHOICES, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

