from django.shortcuts import render
from form.models import Profile

# from django.core.exceptions import BadRequest
# from django.core.exceptions import PermissionDenied
# from django.http import Http404

def index(request):
    profile = None
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()

    # raise BadRequest()          # 400 Bad Request
    # raise PermissionDenied()    # 403 Forbidden
    # raise Http404()             # 404 Not Found
    # raise Exception()           # 500 Internal Server Error 

    return render(request, "home/index.html", {
        "profile": profile,
    })
