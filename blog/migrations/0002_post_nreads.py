# Generated by Django 2.1 on 2018-08-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='nreads',
            field=models.IntegerField(default=0, verbose_name='Número Leituras'),
        ),
    ]
