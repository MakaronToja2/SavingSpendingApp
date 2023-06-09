# Generated by Django 4.2.1 on 2023-06-15 10:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userprofile_currencies_alter_userprofile_user'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Savings', '0005_savingmodelaccess_user_profile_savingmodel_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='accounts_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserSaving',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='savingmodel',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='savingmodel',
            name='users',
        ),
        migrations.DeleteModel(
            name='SavingModelAccess',
        ),
        migrations.AddField(
            model_name='usersaving',
            name='currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Savings.savingmodel'),
        ),
        migrations.AddField(
            model_name='usersaving',
            name='user_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Savings.userprofile'),
        ),
    ]
