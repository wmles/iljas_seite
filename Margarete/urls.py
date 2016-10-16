from django.conf.urls import url

from . import views

app_name = 'Margarete'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^Fachbereiche/(?P<Bezeichnung>[a-z-, A-Z_, 0-9]+)/$', views.UebersichtFachbereich, name='Fachbereich'),
    url(r'^Fachbereiche/(?P<Bezeichnung>[a-z-, A-Z_, 0-9]+)/(?P<BezeichnungWettbewerb>[a-z-, A-Z_, 0-9]+)/$', views.UebersichtWettbewerb, name='Wettbewerb'),
    url(r'^Fachbereiche/(?P<Bezeichnung>[a-z-, A-Z_, 0-9]+)/(?P<BezeichnungWettbewerb>[a-z-, A-Z_, 0-9]+)/(?P<NrRunde>[0-9]+)/$', views.UebersichtWettbewerbsrunde, name='Wettbewerbsrunde'),
    url(r'^Fachbereiche/(?P<Bezeichnung>[a-z-, A-Z_, 0-9]+)/(?P<BezeichnungWettbewerb>[a-z-, A-Z_, 0-9]+)/(?P<NrRunde>[0-9]+)/(?P<NrJahrgang>[0-9]+)/$', views.UebersichtKonkreteWettbewerbsrunde, name='KonkreteWettbewerbsrunde'),
    url(r'^Fachbereiche/(?P<Bezeichnung>[a-z-, A-Z_, 0-9]+)/(?P<BezeichnungWettbewerb>[a-z-, A-Z_, 0-9]+)/Jahrgang(?P<NrJahrgang>[0-9]+)/$', views.UebersichtWettbewerbsjahrgang, name='Wettbewerbsjahrgang'),
    url(r'^Veranstaltungen/(?P<Bezeichnung>[a-z-, A-Z_, 0-9]+)/$', views.UebersichtVeranstaltung, name='Veranstaltung'),
    url(r'^Person/(?P<Bezeichnung>[a-z-, A-Z_, 0-9]+)/$', views.Profilseite, name='Profil'),
    url(r'^Seminare/(?P<Bezeichnung>[a-z-, A-Z_, 0-9]+)/$', views.UebersichtSeminar, name='Seminar'),
    url(r'^Veranstaltungen/(?P<Bezeichnung>[a-z-, A-Z_, 0-9]+)/TeilnahmeeintragenSubmit/$', views.Teilnahmeeintragensubmit, name='Tsubmit'),
    url(r'^Veranstaltungen/(?P<urlVeranstaltung>[a-z-, A-Z_, 0-9]+)/Teilnahmeeintragen/$', views.Teilnahmeeintragen, name='Teintragen'),
    url(r'^Veranstaltungen/$', views.UebersichtVeranstaltungen, name='Veranstaltungen'),
    
    
]