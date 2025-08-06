from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class HomeStaticSitemap(Sitemap):
    changefreq = "yearly"
    priority = 1.0

    def items(self):
        return ["home:index"]

    def location(self, item):
        return reverse(item)
