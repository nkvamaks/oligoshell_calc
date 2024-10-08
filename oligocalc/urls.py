from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'oligocalc'

urlpatterns = [
    path('', views.calc_view, name='calculator'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('success/', views.success, name='success'),
    path('modifications/', views.modifications, name='modifications'),
    # path('taqman_find/', views.taqman_find, name='taqman_find'),
    path('taqman_find/', views.TaqManFindView.as_view(), name='taqman_find'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
