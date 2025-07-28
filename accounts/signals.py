from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from form.models import Profile

@receiver(user_logged_in)
def create_profile_if_missing(sender, request, user, **kwargs):
    Profile.objects.get_or_create(user=user)
