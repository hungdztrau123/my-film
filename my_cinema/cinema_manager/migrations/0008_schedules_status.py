# Generated by Django 4.2.14 on 2024-09-16 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema_manager', '0007_pay_bank_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedules',
            name='status',
            field=models.CharField(choices=[('Có hiệu lực', 'valid'), ('Hết hạn', 'expire')], default='Có hiệu lực', max_length=100),
        ),
    ]