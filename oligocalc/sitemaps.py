from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.7
    changefreq = "weekly"

    def items(self):
        return ['oligocalc:calculator',
                'oligocalc:about',
                'oligocalc:contact',
                'oligocalc:modifications',
                'oligocalc:taqman_find']

    def location(self, item):
        return reverse(item)
