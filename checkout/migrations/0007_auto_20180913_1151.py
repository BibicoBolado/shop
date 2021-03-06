# Generated by Django 2.1 on 2018-09-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_order_valortotal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='valorTotal',
        ),
        migrations.AddField(
            model_name='order',
            name='rastreio',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Código Rastreio'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(blank=True, choices=[(0, 'Aguardando Pagamento'), (1, 'Compra Concluida'), (2, 'Compra Cancelada'), (3, 'Está Chegando!')], default=0, verbose_name='Situação'),
        ),
    ]
