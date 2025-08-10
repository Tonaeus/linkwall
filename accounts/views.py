from django.shortcuts import render, redirect
from form.models import Profile
from .forms import CustomUserCreationForm

def signup_view(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect("accounts:login")
    else:
        form = CustomUserCreationForm()

    return render(request, "accounts/signup.html", {"form": form})
