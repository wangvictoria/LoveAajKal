# Generated by Django 3.2.8 on 2021-11-15 04:17

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoveAajKalApp', '0007_auto_20211106_1228'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='age',
        ),
        migrations.AddField(
            model_name='profile',
            name='birthdate',
            field=models.DateField(default=datetime.date(1900, 1, 1), validators=[django.core.validators.MinValueValidator(datetime.date(1900, 1, 1)), django.core.validators.MaxValueValidator(datetime.date(2003, 11, 15))]),
        ),
    ]