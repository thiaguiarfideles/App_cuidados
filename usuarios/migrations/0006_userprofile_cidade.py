# Generated by Django 2.0.6 on 2020-06-06 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_userprofile_telefone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='cidade',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Cidade'),
        ),
    ]
