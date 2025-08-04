from django.shortcuts import render, get_object_or_404
from form.models import Profile

def user_profile(request, slug):
    profile = get_object_or_404(Profile, slug=slug)
    links = profile.links.all()

    return render(request, "user/user_profile.html", {
        "profile": profile,
        "links": links,
    })
