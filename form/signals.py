import os
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils import timezone
from .models import Profile, Link

@receiver(post_delete, sender=Profile)
def delete_avatar_on_delete_profile(sender, instance, **kwargs):
    if instance.avatar and instance.avatar.path:
        if os.path.isfile(instance.avatar.path):
            os.remove(instance.avatar.path)

@receiver(post_save, sender=Link)
def update_profile_updated_at_on_link_save(sender, instance, **kwargs):
    Profile.objects.filter(pk=instance.profile.pk).update(updated_at=timezone.now())

@receiver(post_delete, sender=Link)
def update_profile_updated_at_on_link_delete(sender, instance, **kwargs):
    Profile.objects.filter(pk=instance.profile.pk).update(updated_at=timezone.now())