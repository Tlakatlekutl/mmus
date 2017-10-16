from django.conf.urls import url
from . import views, api
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)$', views.images, name='images'),
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/upload$', views.upload, name='upload'),
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/download$', views.download, name='download'),    
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/result$', views.result, name='result'),   
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/(?P<image>[0-9]+)/markup$', views.markup, name='markup'),
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/(?P<image>[0-9]+)/next$', views.next, name='next'),          
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/(?P<image>[0-9]+)/toggle$', views.toggle, name='toggle'),    
    url(r'^api/login$', api.login_user, name='api.login'),
    url(r'^api/user$', api.signup, name='api.signup'),
    url(r'^api/logout$', api.logout_user, name='api.logout'),
    url(r'^api/category$', api.category, name='api.category'),
    url(r'^api/upload$', api.upload, name='api.upload'),
    url(r'^api/result$', api.result, name='api.result'),
    url(r'^api/image$', api.image, name='api.image'),
    url(r'^api/markup$', api.markup, name='api.markup'),        
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


