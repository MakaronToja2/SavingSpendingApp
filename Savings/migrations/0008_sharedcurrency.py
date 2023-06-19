# Generated by Django 4.2.1 on 2023-06-19 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Savings', '0007_alter_usersaving_user_profile_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='SharedCurrency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(choices=[('WSP', 'Wspolne')], max_length=3, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
    ]
