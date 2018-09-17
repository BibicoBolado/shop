# Generated by Django 2.1 on 2018-09-16 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20180913_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Rua, Estrada ou Avenida *'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bairro',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Bairro *'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, max_length=400, null=True, verbose_name='Descrição *'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cep',
            field=models.IntegerField(blank=True, null=True, verbose_name='CEP *'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='cidate',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Cidade *'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='complemento',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Complemento *'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Nome *'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Número *'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='uf',
            field=models.CharField(blank=True, choices=[('AC', 'AC'), ('AL', 'AL'), ('AM', 'AM'), ('AP', 'AP'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MG', 'MG'), ('MS', 'MS'), ('MT', 'MT'), ('PA', 'PA'), ('PB', 'PB'), ('PE', 'PE'), ('PI', 'PI'), ('PR', 'PR'), ('RJ', 'RJ'), ('RN', 'RN'), ('RO', 'RO'), ('RR', 'RR'), ('RS', 'RS'), ('SC', 'SC'), ('SE', 'SE'), ('SP', 'SP'), ('TC', 'TC')], default='RJ', max_length=2, null=True, verbose_name='UF *'),
        ),
    ]