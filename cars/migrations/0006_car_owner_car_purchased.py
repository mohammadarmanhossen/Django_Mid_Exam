# Generated by Django 5.0.7 on 2024-08-25 00:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_car_price'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owned_cars', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='car',
            name='purchased',
            field=models.BooleanField(default=False),
        ),
    ]