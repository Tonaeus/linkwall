from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from form.models import Profile

class UserProfileSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Profile.objects.all()
    
    def location(self, obj):
        return reverse('user:user_profile', kwargs={'slug': obj.slug})

    def lastmod(self, obj):
        return obj.updated_at 
