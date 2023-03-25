from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'oligocalc'

urlpatterns = [
    path('', views.calc_view, name='calculator'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
