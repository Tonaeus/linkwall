import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Profile

@receiver(post_delete, sender=Profile)
def delete_avatar_on_delete(sender, instance, **kwargs):
    print("test")
    if instance.avatar and instance.avatar.path:
        if os.path.isfile(instance.avatar.path):
            os.remove(instance.avatar.path)
