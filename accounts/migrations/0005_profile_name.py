# Generated by Django 2.1 on 2018-08-28 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180827_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.CharField(default='Fulana(o)', max_length=150, verbose_name='Nome'),
        ),
    ]
