from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)$', views.images, name='images'),
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/upload$', views.upload, name='upload'),
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/result$', views.result, name='result'),   
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/(?P<image>[0-9]+)/markup$', views.markup, name='markup'),          
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


