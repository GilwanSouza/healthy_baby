# Generated by Django 5.1.5 on 2025-02-17 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthybaby', '0017_odonto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='odonto',
            name='calculo_dentario',
            field=models.CharField(blank=True, choices=[('', 'Selecione'), ('sim', 'Sim'), ('nao', 'Não')], max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='odonto',
            name='mobilidade',
            field=models.CharField(blank=True, choices=[('', 'Selecione'), ('sim', 'Sim'), ('nao', 'Não')], max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='odonto',
            name='perda_insercao',
            field=models.CharField(blank=True, choices=[('', 'Selecione'), ('sim', 'Sim'), ('nao', 'Não')], max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='odonto',
            name='placa_sangramento',
            field=models.CharField(blank=True, choices=[('', 'Selecione'), ('sim', 'Sim'), ('nao', 'Não')], max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='odonto',
            name='placa_sangramento_sondagem',
            field=models.CharField(blank=True, choices=[('', 'Selecione'), ('sim', 'Sim'), ('nao', 'Não')], max_length=55, null=True),
        ),
        migrations.AlterField(
            model_name='odonto',
            name='placa_viavel',
            field=models.CharField(blank=True, choices=[('', 'Selecione'), ('sim', 'Sim'), ('nao', 'Não')], max_length=55, null=True),
        ),
    ]
