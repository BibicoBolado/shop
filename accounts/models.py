# coding=utf-8
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user        = models.OneToOneField(User,on_delete=models.CASCADE,blank=True,null=True)
    name        = models.CharField('Nome',max_length=150,default="Fulana(o)")
    bio         = models.TextField('Descrição',max_length=400,blank=True,null=True)
    birthday    = models.DateField('Aniversário (aaaa-mm-dd)',null=True,blank=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()