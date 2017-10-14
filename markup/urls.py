from django.conf.urls import url
from . import views, api
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)$', views.images, name='images'),
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/upload$', views.upload, name='upload'),
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/result$', views.result, name='result'),   
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/(?P<image>[0-9]+)/markup$', views.markup, name='markup'),
    url(r'^category/(?P<category>[a-zA-Z0-9_а-яА-Я ]+)/(?P<image>[0-9]+)/next$', views.next, name='next'),          
    url(r'^api/login$', api.login_user, name='login'),
    url(r'^api/user$', api.signup, name='signup'),
    url(r'^api/logout$', api.logout_user, name='logout'),
    
    
              
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


