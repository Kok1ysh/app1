# Generated by Django 4.2.14 on 2024-07-25 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultys',
            name='dean',
            field=models.CharField(max_length=50, verbose_name='Декан факультету'),
        ),
    ]
