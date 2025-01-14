

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import User, Sponsor

@receiver(post_save, sender=User)
def post_save_create_profile(sender, instance, created, **kwargs):
    if created:
        Sponsor.objects.create(user=instance)
