import re
from django import forms
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from form.models import Profile

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data.get("username")

        if not re.fullmatch(r"[a-zA-Z0-9\-]+", username):
            raise forms.ValidationError(
                "Enter a valid username. This value may contain only letters, numbers, and hyphens. "
            )

        slug = slugify(username)
        if Profile.objects.filter(slug=slug).exists():
            raise forms.ValidationError(
                "A user with that username already exists. "
            )

        return username
