from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponseNotAllowed
from .models import Profile, Link
from .forms import ProfileForm, LinkForm
from django.forms import inlineformset_factory

@login_required
def edit(request):
    profile = get_object_or_404(Profile, user=request.user)

    links_limit = 5
    links_count = profile.links.count()

    LinkFormSet = inlineformset_factory(
        Profile, Link,
        form=LinkForm,
        fields=['label', 'url'],
        extra=max(0, links_limit - links_count),
        max_num=links_limit,
        can_delete=False,
    )

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        link_formset = LinkFormSet(request.POST, instance=profile)

        if profile_form.is_valid() and link_formset.is_valid():
            profile_form.save()
            link_formset.save()
            return redirect("form:edit") 
    else:
        profile_form = ProfileForm(instance=profile)
        link_formset = LinkFormSet(instance=profile)

    return render(request, "form/edit.html", {
        "profile_form": profile_form,
        "link_formset": link_formset,
    })
