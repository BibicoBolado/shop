# coding=utf-8
from django.db import models

class CategoryCatalog(models.Model):
    name     =      models.CharField('Nome',max_length = 150)
    slug     =      models.SlugField('Atalho',max_length=150)
    description =      models.TextField('Descrição',blank=True,null=True)
    created  =      models.DateTimeField('Criado em:',auto_now_add=True)
    modified =      models.DateTimeField('Atualizado em:',auto_now=True)
    

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['name']

    def __str__(self):
        return self.name

class Project(models.Model):
    selection = (
        (1,'Normal'),
        (2,'Destaque'),
    )
    name        =      models.CharField('Nome',max_length = 150)
    slug        =      models.SlugField('Atalho',max_length=150)
    category    =      models.ForeignKey('catalog.CategoryCatalog',verbose_name='Categoria',on_delete=models.CASCADE)
    description =      models.TextField('Descrição',blank=True)
    created     =      models.DateTimeField('Criado em:',auto_now_add=True)
    modified    =      models.DateTimeField('Atualizado em:',auto_now=True)
    imagemin    =      models.ImageField(upload_to='catalog/imagesmin',
                        verbose_name='Imagem',null=True,blank=True
    )

    class Meta:
        verbose_name = 'Projetos'
        verbose_name_plural = 'Projeto'
        ordering = ['name']

    def __str__(self):
        return self.name

class Image(models.Model):
    image       =       models.ImageField(upload_to='catalog/images',
                        verbose_name='Imagem',null=True,blank=True
    )
    name        =       models.CharField('Nome',max_length=150)
    description =       models.TextField('Descrição')
    created     =      models.DateTimeField('Criado em:',auto_now_add=True)
    modified    =      models.DateTimeField('Atualizado em:',auto_now=True)
    project     =      models.ForeignKey('catalog.Project',verbose_name='Projeto',on_delete=models.CASCADE,
                       null=True,blank=True)

    class Meta:
        verbose_name = 'Imagens'
        verbose_name_plural = 'Image'
        ordering = ['name']

    def __str__(self):
        return self.name
