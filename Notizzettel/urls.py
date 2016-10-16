from django.conf.urls import include, url
from . import views

app_name = 'Notizzettel'
urlpatterns = [
    url('^$', views.IndexView.as_view(), name='index'), 
    url('^eintragen/$', views.Eintragen, name='eintragen'), 
]
