# Generated by Django 5.1.5 on 2025-02-08 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('healthybaby', '0006_alter_gestante_emg_ctt_parentesco_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gestante',
            name='idade_gestacional',
        ),
    ]
