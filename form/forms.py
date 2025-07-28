from django import forms
from django.forms import inlineformset_factory
from .models import Profile, Link

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'bio', 'avatar']

LinkFormSet = inlineformset_factory(
    Profile,
    Link,
    fields=['label', 'url', 'order'],
    extra=1,  # number of blank forms shown
    can_delete=True,
    max_num=5,  # maximum number of links allowed
    validate_max=True,
)
