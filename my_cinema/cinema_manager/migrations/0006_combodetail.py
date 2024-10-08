# Generated by Django 4.2.14 on 2024-09-14 05:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cinema_manager', '0005_background'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComboDetail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(db_index=True, default=django.utils.timezone.now)),
                ('booking', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_manager.bookings')),
                ('combo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cinema_manager.combo')),
                ('create_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_created', to=settings.AUTH_USER_MODEL)),
                ('editor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_editor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
