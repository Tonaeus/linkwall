from django.shortcuts import render, get_object_or_404
from form.models import Profile
from django.forms.models import model_to_dict

def user_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    links = [link for link in profile.links.all() if link.label and link.url]

    print(model_to_dict(profile))

    return render(request, "user/user_profile.html", {
        "profile": profile,
        "links": links,
    })
