# Generated by Django 4.2.14 on 2024-09-16 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0002_alter_facultys_dean'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kafedras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleKafedra', models.CharField(max_length=75, verbose_name='Назва')),
                ('adresKafedra', models.CharField(max_length=150, verbose_name='Адреса факультету')),
                ('managerKafedra', models.CharField(max_length=50, verbose_name='Декан факультету')),
                ('facultyKafedra', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='control.facultys')),
            ],
        ),
    ]