# Generated by Django 5.1.2 on 2024-11-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_benhnhan_mabaohiemyte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hosobenhan',
            name='thoiGianKham',
            field=models.DateField(auto_created=True),
        ),
    ]