# Generated by Django 5.1.5 on 2025-02-08 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthybaby', '0004_gestante_cep_gestante_cidade_gestante_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestante',
            name='endereco',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='gestante',
            name='ponto_referencia',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
