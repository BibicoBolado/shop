# Generated by Django 2.1 on 2018-08-28 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20180827_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Aniversário (aaaa-dd-mm)'),
        ),
    ]
