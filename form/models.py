from django.db import models
from django.contrib.auth.models import User
from utils.file_utils import avatar_upload_to
from django.templatetags.static import static

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    avatar = models.ImageField(upload_to=avatar_upload_to, blank=True)
    name = models.CharField(max_length=127)
    biography = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Link(models.Model):
    profile = models.ForeignKey(Profile, related_name="links", on_delete=models.CASCADE)
    label = models.CharField(max_length=127, blank=True)
    url = models.URLField(blank=True)

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.label} ({self.url})"
