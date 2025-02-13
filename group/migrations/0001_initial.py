# Generated by Django 4.2.14 on 2024-09-28 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('educational_programs', '0002_alter_komponenteducationalprograms_kodnd'),
        ('control', '0008_remove_komponenteducationalprograms_educationalprogram_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Groups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, verbose_name='Назва')),
                ('titleFull', models.CharField(max_length=150, verbose_name='Повна назва')),
                ('kurs', models.PositiveIntegerField(default=1)),
                ('educational_programs', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='educational_programs.educationalprograms')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control.facultys')),
            ],
        ),
    ]
