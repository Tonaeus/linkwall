from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from form.models import Profile

def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)
            return redirect("accounts:login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})
