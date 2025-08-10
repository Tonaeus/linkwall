from django import forms
from .models import Profile, Link
import os

class CustomFileInput(forms.ClearableFileInput):
    template_name = 'form/widgets/custom_file_input.html' 

class ProfileForm(forms.ModelForm):
    avatar = forms.ImageField(widget=CustomFileInput(), required=False)

    class Meta:
        model = Profile
        fields = ['avatar', 'name', 'biography']
    
    def save(self, commit=True):
        profile = super().save(commit=False)
        
        if profile.pk:
            old_avatar = Profile.objects.get(pk=profile.pk).avatar
            new_avatar = self.cleaned_data.get('avatar')

            if not new_avatar and old_avatar:
                if os.path.isfile(old_avatar.path):
                    os.remove(old_avatar.path)
                profile.avatar = None

        if commit:
            profile.save()

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['label', 'url']

    def clean_label(self):
        label = self.cleaned_data.get('label', '')
        return label.strip() if label else label

    def clean_url(self):
        url = self.cleaned_data.get('url', '')
        return url.strip() if url else url

    def clean(self):
        cleaned_data = super().clean()
        label = cleaned_data.get('label', '').strip()
        url = cleaned_data.get('url', '').strip()

        if label == '' and url == '':
            self.cleaned_data['DELETE'] = True
            
        return cleaned_data
