# Generated by Django 2.0.6 on 2018-07-12 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestadores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestadorpessoafisica',
            name='nm_completo',
            field=models.CharField(default='test', max_length=100, verbose_name='Nome Completo'),
            preserve_default=False,
        ),
    ]
