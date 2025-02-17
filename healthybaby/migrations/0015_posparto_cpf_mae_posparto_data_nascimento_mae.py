# Generated by Django 5.1.5 on 2025-02-17 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthybaby', '0014_posparto_remove_gestante_alta_maternidade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='posparto',
            name='cpf_mae',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AddField(
            model_name='posparto',
            name='data_nascimento_mae',
            field=models.DateField(blank=True, null=True),
        ),
    ]
