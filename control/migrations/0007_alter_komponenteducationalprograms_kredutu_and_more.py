# Generated by Django 4.2.14 on 2024-09-21 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0006_formakontrolus_komponenteducationalprograms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='komponenteducationalprograms',
            name='kredutu',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='komponenteducationalprograms',
            name='semestr',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
