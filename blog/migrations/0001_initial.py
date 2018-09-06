# Generated by Django 2.1 on 2018-08-14 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=100, verbose_name='Atalho')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualizado em:')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Nome')),
                ('slug', models.SlugField(max_length=150, verbose_name='Atalho')),
                ('about', models.TextField(verbose_name='Resumo')),
                ('text', models.TextField(verbose_name='Texto. Coloca o Coração Nisso')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em:')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Atualizado em:')),
                ('featured', models.IntegerField(choices=[(1, 'Normal'), (2, 'Destaque')], default=1, max_length=2, verbose_name='Destaque')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='blog/images', verbose_name='Imagem')),
                ('imgfeat', models.ImageField(blank=True, null=True, upload_to='blog/images/destaque', verbose_name='Imagem Destaque')),
                ('imgcapa', models.ImageField(blank=True, null=True, upload_to='blog/images/destaque', verbose_name='Imagem Capa')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Category', verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Produtos',
                'verbose_name_plural': 'Produto',
                'ordering': ['name'],
            },
        ),
    ]