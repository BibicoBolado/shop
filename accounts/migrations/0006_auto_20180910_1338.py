# Generated by Django 2.1 on 2018-09-10 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_profile_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Endereço'),
        ),
        migrations.AddField(
            model_name='profile',
            name='cep',
            field=models.IntegerField(blank=True, null=True, verbose_name='CEP'),
        ),
        migrations.AddField(
            model_name='profile',
            name='complemento',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Complemento'),
        ),
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número'),
        ),
        migrations.AddField(
            model_name='profile',
            name='uf',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Estado'),
        ),
    ]
