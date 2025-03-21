# Generated by Django 5.1.5 on 2025-02-13 12:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthybaby', '0012_alter_gestante_cpf'),
    ]

    operations = [
        migrations.AddField(
            model_name='gestante',
            name='alta_maternidade',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='data_nascimento_bebe',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='intercorrencias',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='local_nascimento',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='medicamentos',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='nascimento',
            field=models.CharField(blank=True, choices=[('', 'Selecione o Parentesco'), ('prematuro', 'Prematuro'), ('atermo', 'A termo')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='nome_bebe',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='nome_mae',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='peso_alta',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='profissionais',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='sangramento',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='tipo_parto',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
        migrations.AddField(
            model_name='gestante',
            name='visita_domiciliar',
            field=models.CharField(blank=True, max_length=55, null=True),
        ),
    ]
