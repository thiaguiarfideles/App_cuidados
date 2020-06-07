# Generated by Django 2.0.6 on 2020-04-20 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestadores', '0013_auto_20200414_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prestadorpessoafisica',
            name='sn_cirurgiao',
        ),
        migrations.AddField(
            model_name='prestadorpessoafisica',
            name='sn_cuidador',
            field=models.NullBooleanField(verbose_name='Cuidador?'),
        ),
        migrations.AddField(
            model_name='prestadorpessoafisica',
            name='sn_paciente',
            field=models.NullBooleanField(verbose_name='Paciente?'),
        ),
    ]
