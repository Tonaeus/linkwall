from django.shortcuts import render
from form.models import Profile

def index(request):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()

    return render(request, "home/index.html", {
        "profile": profile,
    })
