# Generated by Django 4.2.14 on 2024-09-21 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_alter_kafedras_adreskafedra_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationalPrograms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Назва')),
                ('riven', models.CharField(max_length=75, verbose_name='Рівень')),
                ('stupin', models.CharField(max_length=75, verbose_name='Ступінь')),
                ('galuz', models.CharField(max_length=75, verbose_name='Галузь знань')),
                ('specialnist', models.CharField(max_length=75, verbose_name='Спеціальність')),
                ('specializaciya', models.CharField(max_length=75, verbose_name='Спеціалізація')),
                ('osvKvalifikaciya', models.CharField(max_length=150, verbose_name='Освітня кваліфікація')),
                ('profKvalifikaciya', models.CharField(max_length=150, verbose_name='Професійна кваліфікація')),
            ],
        ),
    ]
