# coding=utf-8
from django.db import models
from django.urls import reverse

class CategoryShop(models.Model):
    name     =      models.CharField('Nome',max_length = 150)
    slug     =      models.SlugField('Atalho',max_length=100)
    description =      models.TextField('Descrição',blank=True,null=True)
    created  =      models.DateTimeField('Criado em:',auto_now_add=True)
    modified =      models.DateTimeField('Atualizado em:',auto_now=True)
    

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name


class Product(models.Model):
    
    selection = (
        (1,'Normal'),
        (2,'Destaque'),
    )

    name        =      models.CharField('Nome',max_length = 150)
    slug        =      models.SlugField('Atalho',max_length=100)
    category    =      models.ForeignKey('shop.CategoryShop',verbose_name='Categoria',on_delete=models.CASCADE)
    description =      models.TextField('Descrição',blank=True)
    price       =      models.DecimalField('Preço',decimal_places=2,max_digits=8)
    created     =      models.DateTimeField('Criado em:',auto_now_add=True)
    modified    =      models.DateTimeField('Atualizado em:',auto_now=True)
    featured    =      models.IntegerField('Destaque',choices=selection,default=1)
    imagem      =      models.ImageField(
        upload_to='produtc/images',verbose_name='Imagem',
        null=True,blank=True
    )
    imgfeat     =models.ImageField(
        upload_to='produtc/images/destaque',verbose_name='Imagem',
        null=True,blank=True
    )
    class Meta:
        verbose_name = 'Produtos'
        verbose_name_plural = 'Produto'
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('core:itenShop', kwargs={'slug':self.slug})