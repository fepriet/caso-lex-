from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Cliente

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(usuario=instance)
    instance.cliente.save()

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.cliente.save()