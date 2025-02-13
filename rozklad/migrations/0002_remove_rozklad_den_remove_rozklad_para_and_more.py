# Generated by Django 4.2.14 on 2024-12-16 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('robochiy_navchalnuy_plan', '0003_alter_elementrnp_formakontrolu1sm_and_more'),
        ('rozklad', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rozklad',
            name='den',
        ),
        migrations.RemoveField(
            model_name='rozklad',
            name='para',
        ),
        migrations.RemoveField(
            model_name='rozklad',
            name='predmet',
        ),
        migrations.AddField(
            model_name='rozklad',
            name='chetver_1_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chetver_1', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='chetver_2_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chetver_2', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='chetver_3_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chetver_3', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='chetver_4_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chetver_4', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='chetver_5_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='chetver_5', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='ponedilok_1_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ponedilok_1', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='ponedilok_2_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ponedilok_2', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='ponedilok_3_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ponedilok_3', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='ponedilok_4_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ponedilok_4', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='ponedilok_5_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='ponedilok_5', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='pyatnytsya_1_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pyatnytsya_1', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='pyatnytsya_2_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pyatnytsya_2', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='pyatnytsya_3_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pyatnytsya_3', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='pyatnytsya_4_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pyatnytsya_4', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='pyatnytsya_5_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='pyatnytsya_5', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='sereda_1_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sereda_1', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='sereda_2_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sereda_2', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='sereda_3_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sereda_3', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='sereda_4_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sereda_4', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='sereda_5_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='sereda_5', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='subota_1_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subota_1', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='subota_2_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subota_2', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='subota_3_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subota_3', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='subota_4_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subota_4', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='subota_5_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='subota_5', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='vivtorok_1_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vivtorok_1', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='vivtorok_2_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vivtorok_2', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='vivtorok_3_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vivtorok_3', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='vivtorok_4_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vivtorok_4', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
        migrations.AddField(
            model_name='rozklad',
            name='vivtorok_5_para',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='vivtorok_5', to='robochiy_navchalnuy_plan.elementrnp'),
        ),
    ]
