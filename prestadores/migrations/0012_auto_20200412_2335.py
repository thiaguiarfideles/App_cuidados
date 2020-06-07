# Generated by Django 2.0.6 on 2020-04-13 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prestadores', '0011_auto_20180715_1435'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2000)),
                ('complete', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'prestadores',
            },
        ),
        migrations.AlterModelOptions(
            name='prestadorpessoafisica',
            options={},
        ),
    ]
