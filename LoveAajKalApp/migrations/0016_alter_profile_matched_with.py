# Generated by Django 3.2.8 on 2021-12-03 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoveAajKalApp', '0015_auto_20211203_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='matched_with',
            field=models.CharField(blank=True, default=' ', max_length=100, null=True),
        ),
    ]