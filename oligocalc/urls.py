from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.sitemaps.views import sitemap


from . import views
from .sitemaps import StaticViewSitemap

app_name = 'oligocalc'

sitemaps = {
    'static': StaticViewSitemap,
}

urlpatterns = [
    path('', views.CalcView.as_view(), name='calculator'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('modifications/', views.modifications, name='modifications'),
    path('taqman_find/', views.TaqManFindView.as_view(), name='taqman_find'),
    path('sirna_score/', views.SirnaScoreView.as_view(), name='sirna_score'),
    path('sirna_score_explained/', views.SirnaScoreExplainedView.as_view(), name='sirna_score_explained'),
    path('profile/details/', views.ProfileDetails.as_view(), name='profile_details'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
