# Generated by Django 4.2.14 on 2024-08-14 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_manager', '0022_alter_seats_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingdetail',
            name='seat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cinema_manager.seats'),
        ),
    ]