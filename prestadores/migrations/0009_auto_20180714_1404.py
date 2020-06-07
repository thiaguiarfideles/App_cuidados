# Generated by Django 2.0.6 on 2018-07-14 17:04

from django.db import migrations, models
import prestadores.models


class Migration(migrations.Migration):

    dependencies = [
        ('prestadores', '0008_auto_20180714_1358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestadorpessoafisica',
            name='comprovante_residencia',
            field=models.FileField(upload_to=prestadores.models.comp_resid_directory_path),
        ),
        migrations.AlterField(
            model_name='prestadorpessoafisica',
            name='identidade_frente',
            field=models.FileField(upload_to=prestadores.models.identidade_frente_directory_path),
        ),
        migrations.AlterField(
            model_name='prestadorpessoafisica',
            name='identidade_verso',
            field=models.FileField(upload_to=prestadores.models.identidade_verso_directory_path),
        ),
    ]
