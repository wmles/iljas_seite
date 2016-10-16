from django.conf.urls import include, url
import django.contrib.auth.urls
from django.contrib.auth import views as auth_views
from . import views

app_name = 'Nutzerverwaltung'
urlpatterns = [
    url('^$', views.IndexView.as_view(), name='index'), 
    url('^Profil/(?P<pk>[0-9]+)/$', views.ProfilView.as_view(), name='Profil'),
    url('^MeinProfil/PasswortAendern$', views.MeinPasswortAendern, name='MeinPasswortAendern'), 
    url('^MeinProfil/$', views.MeinProfilAnzeigen, name='MeinProfil'), 
    url('^login/$', auth_views.login, {'template_name': 'Nutzerverwaltung/login.html'}, name='login'), 
    url('^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'), 
    url('^register/$', views.Registrieren_Anfordern, name='register'), 
    url('^register/Erstellen/$', views.Registrieren_MailSenden, name='register_confirm'), 
    url('^', include('django.contrib.auth.urls')),
]
