# Generated by Django 3.2.8 on 2021-11-06 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoveAajKalApp', '0005_auto_20211106_1203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='notes',
            field=models.CharField(blank=True, default='', max_length=500, null=True),
        ),
    ]
