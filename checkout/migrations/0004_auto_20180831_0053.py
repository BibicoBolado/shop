# Generated by Django 2.1 on 2018-08-31 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0003_order_orderiten'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartiten',
            name='cart_id',
            field=models.CharField(db_index=True, max_length=40, null=True, verbose_name='Chave do Carrinho'),
        ),
    ]