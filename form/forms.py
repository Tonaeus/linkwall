from django import forms
from .models import Profile, Link

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'name', 'bio']

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['label', 'url']
