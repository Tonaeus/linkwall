from django.db import models
from django.contrib.auth.models import User
from utils.file_utils import avatar_upload_to

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=127)
    biography = models.TextField(blank=True)
    avatar = models.ImageField(upload_to=avatar_upload_to, blank=True)

    def __str__(self):
        return self.user.username

class Link(models.Model):
    profile = models.ForeignKey(Profile, related_name="links", on_delete=models.CASCADE)
    label = models.CharField(max_length=127)
    url = models.URLField()

    class Meta:
        ordering = ["id"]

    def __str__(self):
        return f"{self.label} ({self.url})"
