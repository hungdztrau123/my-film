# Generated by Django 4.2.14 on 2024-08-06 04:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_manager', '0002_alter_place_latitude_alter_place_longitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='dayshow',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema_manager.dayshow'),
        ),
    ]