# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required

# @login_required
# def index(request):
    # return render(request, "form/index.html")

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm, LinkFormSet

@login_required
def index(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        formset = LinkFormSet(request.POST, instance=profile)
        
        if profile_form.is_valid() and formset.is_valid():
            profile_form.save()
            formset.save()
            return redirect('/')  # Or replace with a named URL like redirect('index')
    else:
        profile_form = ProfileForm(instance=profile)
        formset = LinkFormSet(instance=profile)
    
    current_links_count = profile.links.count()
    max_links = 5
    # Always allow save so users can edit or delete links
    can_add_more = current_links_count < max_links
    
    return render(request, 'form/index.html', {
        'profile_form': profile_form,
        'formset': formset,
        'can_add_more': can_add_more,
        'max_links': max_links,
        'current_links_count': current_links_count,
    })
