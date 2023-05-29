from django.db import models

# Create your models here.
class SavingModel(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=[
        ('category1', 'Category 1'),
        ('category2', 'Category 2'),
        ('category3', 'Category 3'),
        # Add more category choices as needed
    ])

    def __str__(self):
        return self.name

    