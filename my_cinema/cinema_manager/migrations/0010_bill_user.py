# Generated by Django 4.2.14 on 2024-09-17 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinema_manager', '0009_remove_pay_bank_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
