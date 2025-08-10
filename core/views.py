from django.http import HttpResponse
from django.urls import reverse

def robots_txt(request):
    sitemap_url = request.build_absolute_uri(reverse("sitemap"))

    lines = [
        "User-Agent: *",
        "Disallow: /",
        "Allow: /",
        "Allow: /user/*",
        "",
        f"Sitemap: {sitemap_url}"
    ]

    return HttpResponse("\n".join(lines), content_type="text/plain")
