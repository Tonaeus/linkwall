from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Profile, Link
from .forms import ProfileForm, LinkForm

@login_required
def edit_profile(request):
    profile = get_object_or_404(Profile, user=request.user)

    links_limit = 5
    links_count = profile.links.count()

    LinkFormSet = inlineformset_factory(
        Profile, Link,
        form=LinkForm,
        fields=['label', 'url'],
        extra=max(0, links_limit - links_count),
        max_num=links_limit,
        can_delete=True,
    )

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        link_formset = LinkFormSet(request.POST, instance=profile)

        if profile_form.is_valid() and link_formset.is_valid():
            profile_form.save()
            link_formset.save()
            return redirect("form:edit_profile") 
    else:
        profile_form = ProfileForm(instance=profile)
        link_formset = LinkFormSet(instance=profile)

    return render(request, "form/edit_profile.html", {
        "profile_form": profile_form,
        "link_formset": link_formset,
    })
