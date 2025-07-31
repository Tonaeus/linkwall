from django import forms
from .models import Profile, Link

class CustomFileInput(forms.ClearableFileInput):
    template_name = 'form/widgets/custom_file_input.html' 

class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=CustomFileInput(), required=False)

    class Meta:
        model = Profile
        fields = ['avatar', 'name', 'biography']

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['label', 'url']
