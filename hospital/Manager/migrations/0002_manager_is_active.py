# Generated by Django 5.0.6 on 2024-11-21 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]