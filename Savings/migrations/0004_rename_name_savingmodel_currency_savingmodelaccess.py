# Generated by Django 4.2.1 on 2023-06-13 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Savings', '0003_remove_savingmodel_category_alter_savingmodel_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='savingmodel',
            old_name='name',
            new_name='currency',
        ),
        migrations.CreateModel(
            name='SavingModelAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Savings.savingmodel')),
            ],
        ),
    ]
