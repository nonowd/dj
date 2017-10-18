from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.home),
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})$', views.list_articles, name = 'list_articles'),
    url(r'^redirection$', views.view_redirection, name = 'view_redirection'),
    url(r'^date$', views.date_actuelle, name='date_actuelle'),
    url(r'^addition/(?P<nombre1>\d+)/(?P<nombre2>\d+)/$', views.addition),
    url(r'^$', views.accueil, name = 'accueil'),
    url(r'^article/(\d+)$', views.lire, name = 'lire')
]