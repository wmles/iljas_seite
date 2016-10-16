# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .models import *

def index(request):
    Fachbereiche = Fachbereich.objects.all()
    ListeNeuesterW = Wettbewerb.objects.order_by('-erstelldatum')[:5]
    ListeNeueV = Veranstaltung.objects.order_by('-erstelldatum')[:5]
    return render(request, 'Margarete/index.html', {'Fachbereiche': Fachbereiche, 'ListeNeuesterW': ListeNeuesterW, 'ListeNeueV':ListeNeueV})

def UebersichtFachbereich(request, Bezeichnung):
    Name = get_object_or_404(Fachbereich, urlbezeichnung=Bezeichnung)
    Seminare = Seminar.objects.filter(fachbereich=Name,gehoertzuwettbewerbsrunde=None)
    #ListeWettbewerbe = Name.wettbewerb_set.all()
    return render(request, 'Margarete/Fachbereich.html', {'Fachbereich': Name, 'Seminare':Seminare})
	
def UebersichtWettbewerb(request, Bezeichnung, BezeichnungWettbewerb):
    NameFachbereich = get_object_or_404(Fachbereich, urlbezeichnung=Bezeichnung)
    NameWettbewerb = get_object_or_404(Wettbewerb, urlbezeichnung=BezeichnungWettbewerb)
    #Bestimmung der vorhandenen Jahrgänge
    ListeKonkreteWettbewerbsrunden = KonkreteWettbewerbsrunde.objects.filter(wettbewerbsrunde__wettbewerb=NameWettbewerb)
    ListeJahrgange = []
    for ii in ListeKonkreteWettbewerbsrunden:
    	if ii.nummer in ListeJahrgange:
    		pass
    	else:
    		ListeJahrgange.append(ii.nummer)
    #Ehrentafel
    ListeTeilnehmer = Person.objects.filter(teilnahme__veranstaltung__wettbewerbsveranstaltung__konkreteWettbewerbsrunde__wettbewerbsrunde__wettbewerb=NameWettbewerb).distinct()
    ScoreListe=[]
    for teilnehmer in ListeTeilnehmer:
    	ListeTeilnahmen = Teilnahme.objects.filter(veranstaltung__wettbewerbsveranstaltung__konkreteWettbewerbsrunde__wettbewerbsrunde__wettbewerb=NameWettbewerb,person=teilnehmer)
    	score = 0
    	for teilnahme in ListeTeilnahmen:
    		if teilnahme.teilnahmeart.wert < 6:
    			score += (6-teilnahme.teilnahmeart.wert)*(teilnahme.veranstaltung.wettbewerbsveranstaltung.konkreteWettbewerbsrunde.wettbewerbsrunde.runde)
    	ScoreListe.append((teilnehmer,score))
    ScoreListe=list(reversed(sorted(ScoreListe,key=lambda x: x[1])))[:10]
    return render(request, 'Margarete/Wettbewerb.html', {'Wettbewerb':NameWettbewerb, 'Jahrgaenge':ListeJahrgange, 'Ehrentafel':ScoreListe})

def UebersichtWettbewerbsrunde(request, Bezeichnung, BezeichnungWettbewerb, NrRunde):
	NameFachbereich = get_object_or_404(Fachbereich, urlbezeichnung=Bezeichnung)
	NameWettbewerb = get_object_or_404(Wettbewerb, urlbezeichnung=BezeichnungWettbewerb)
	KonkreteRunde = get_object_or_404(Wettbewerbsrunde, runde=NrRunde, wettbewerb=NameWettbewerb)
	#print Bezeichnung, BezeichnungWettbewerb, NrRunde

	#Ehrentafel
	ListeTeilnehmer = Person.objects.filter(teilnahme__veranstaltung__wettbewerbsveranstaltung__konkreteWettbewerbsrunde__wettbewerbsrunde=KonkreteRunde).distinct()
	ScoreListe=[]
	for teilnehmer in ListeTeilnehmer:
		ListeTeilnahmen = Teilnahme.objects.filter(veranstaltung__wettbewerbsveranstaltung__konkreteWettbewerbsrunde__wettbewerbsrunde=KonkreteRunde,person=teilnehmer)
		score = 0
		for teilnahme in ListeTeilnahmen:
			if teilnahme.teilnahmeart.wert < 6:
				score += (6-teilnahme.teilnahmeart.wert)#*(teilnahme.veranstaltung.wettbewerbsveranstaltung.konkreteWettbewerbsrunde.wettbewerbsrunde.runde)
		ScoreListe.append((teilnehmer,score))
	ScoreListe=list(reversed(sorted(ScoreListe,key=lambda x: x[1])))[:5]

	return render(request, 'Margarete/Wettbewerbsrunde.html', {'Fachbereich': NameFachbereich, 'Wettbewerb':NameWettbewerb, 'Wettbewerbsrunde':KonkreteRunde, 'Ehrentafel':ScoreListe})

def UebersichtKonkreteWettbewerbsrunde(request, Bezeichnung, BezeichnungWettbewerb, NrRunde, NrJahrgang):
	NameFachbereich = get_object_or_404(Fachbereich, urlbezeichnung=Bezeichnung)
	NameWettbewerb = get_object_or_404(Wettbewerb, urlbezeichnung=BezeichnungWettbewerb)
	NameWettbewerbsrunde = get_object_or_404(Wettbewerbsrunde, runde=NrRunde, wettbewerb=NameWettbewerb)
	NameKonkreteWettbewerbsrunde = get_object_or_404(KonkreteWettbewerbsrunde, nummer=NrJahrgang, wettbewerbsrunde=NameWettbewerbsrunde)
	ListeTeilnahmen = Teilnahme.objects.filter(veranstaltung__wettbewerbsveranstaltung__konkreteWettbewerbsrunde=NameKonkreteWettbewerbsrunde).distinct()
	ListeTeilnahmen = sorted(ListeTeilnahmen, key=lambda teiln: teiln.teilnahmeart.wert)
	if Wettbewerbsveranstaltung.objects.filter(konkreteWettbewerbsrunde=NameKonkreteWettbewerbsrunde).__len__()==1:
		return HttpResponseRedirect(reverse('Margarete:Veranstaltung',args=(Wettbewerbsveranstaltung.objects.filter(konkreteWettbewerbsrunde=NameKonkreteWettbewerbsrunde)[0],)))#UebersichtVeranstaltung(request,Wettbewerbsveranstaltung.objects.filter(konkreteWettbewerbsrunde=NameKonkreteWettbewerbsrunde)[0])
	return render(request, 'Margarete/KonkreteWettbewerbsrunde.html', {'KonkreteWettbewerbsrunde':NameKonkreteWettbewerbsrunde, 'Teilnahmeliste':ListeTeilnahmen})
    

def UebersichtVeranstaltung(request, Bezeichnung):
	dieVeranstaltung = get_object_or_404(Veranstaltung, urlbezeichnung=Bezeichnung)
	ListeTeilnahmen = Teilnahme.objects.filter(veranstaltung=dieVeranstaltung).distinct()
	ListeTeilnahmen = sorted(ListeTeilnahmen, key=lambda teiln: teiln.teilnahmeart.wert)
	Veranstaltungstyp = 0
	redirected = False
	try:
		dieVeranstaltung.wettbewerbsveranstaltung
	except Wettbewerbsveranstaltung.DoesNotExist:
		try:
			dieVeranstaltung.konkretesseminar
		except KonkretesSeminar.DoesNotExist:
			pass	
		else:
			Veranstaltungstyp = 1
	else:
		Veranstaltungstyp = 2
		if Wettbewerbsveranstaltung.objects.filter(konkreteWettbewerbsrunde=KonkreteWettbewerbsrunde.objects.get(wettbewerbsveranstaltung__veranstaltung_ptr=dieVeranstaltung)).__len__()==1:
			redirected = True
	return render(request, 'Margarete/Veranstaltung.html', {'Veranstaltung':dieVeranstaltung,'Teilnahmeliste':ListeTeilnahmen, 'Typ':Veranstaltungstyp, 'redirected':redirected})

def UebersichtWettbewerbsjahrgang(request, Bezeichnung, BezeichnungWettbewerb, NrJahrgang):
	NameFachbereich = get_object_or_404(Fachbereich, urlbezeichnung=Bezeichnung)
	NameWettbewerb = get_object_or_404(Wettbewerb, urlbezeichnung=BezeichnungWettbewerb)
	ListeKonkreteWettbewerbsrunden = KonkreteWettbewerbsrunde.objects.filter(wettbewerbsrunde__wettbewerb=NameWettbewerb,nummer=NrJahrgang)
	ListeRunden = []
	for ii in ListeKonkreteWettbewerbsrunden:
		ListeRunden.append(ii.wettbewerbsrunde.runde)
	return render(request, 'Margarete/JahrgangWettbewerb.html', {'Jahrgang':NrJahrgang, 'Wettbewerb':NameWettbewerb, 'KonkreteWettbewerbsrunden':ListeKonkreteWettbewerbsrunden})
	#return HttpResponse("Ich kenne folgende Runden: %s" % (str(ListeRunden)))

def Profilseite(request, Bezeichnung):
	diePerson = get_object_or_404(Person, urlbezeichnung=Bezeichnung)
	ListeWettbewerbe = Wettbewerb.objects.filter(wettbewerbsrunde__konkretewettbewerbsrunde__wettbewerbsveranstaltung__veranstaltung_ptr__teilnehmer=diePerson,wettbewerbsrunde__konkretewettbewerbsrunde__wettbewerbsveranstaltung__veranstaltung_ptr__teilnahme__teilnahmeart__wert__lte=5).distinct()
	ListeWettbewerbsjahrgange = []
	ListeerreichteRunde = []
	for wettbewerb in ListeWettbewerbe:
		ListeKonkreteWettbewerbsrunden = KonkreteWettbewerbsrunde.objects.filter(wettbewerbsrunde__wettbewerb=wettbewerb,wettbewerbsveranstaltung__veranstaltung_ptr__teilnehmer=diePerson,wettbewerbsveranstaltung__veranstaltung_ptr__teilnahme__teilnahmeart__wert__lte=5)
		ListeJahrgange = []
		for ii in ListeKonkreteWettbewerbsrunden:
			if ii.nummer in ListeJahrgange:
				pass
		 	else:
				ListeJahrgange.append(ii.nummer)
		ListeWettbewerbsjahrgange.append((wettbewerb,ListeJahrgange))
		for jahr in ListeJahrgange:
			ListeKonkreteWettbewerbsrunden = KonkreteWettbewerbsrunde.objects.filter(wettbewerbsrunde__wettbewerb=wettbewerb,wettbewerbsveranstaltung__veranstaltung_ptr__teilnehmer=diePerson,nummer=jahr,wettbewerbsveranstaltung__veranstaltung_ptr__teilnahme__teilnahmeart__wert__lte=5)
			erreichteRunde = 1
			for ii in ListeKonkreteWettbewerbsrunden:
				if ii.wettbewerbsrunde.runde > erreichteRunde:
					erreichteRunde = ii.wettbewerbsrunde.runde
			ListeerreichteRunde.append(get_object_or_404(KonkreteWettbewerbsrunde, wettbewerbsrunde__wettbewerb=wettbewerb,wettbewerbsrunde__runde=erreichteRunde,nummer=jahr))
	ListeTeilnahmen = []
	for kWbr in ListeerreichteRunde:
		ListeTeilnahmen.append(get_object_or_404(Teilnahme,person=diePerson,veranstaltung__wettbewerbsveranstaltung__konkreteWettbewerbsrunde=kWbr))
	ListeVTeilnahmen = Teilnahme.objects.filter(person=diePerson).distinct()
	ListesonstigeTeilnahmen = []
	for teilnahme in ListeVTeilnahmen:
		try:
			teilnahme.veranstaltung.wettbewerbsveranstaltung
		except Wettbewerbsveranstaltung.DoesNotExist:
			ListesonstigeTeilnahmen.append(teilnahme)

	return render(request, 'Margarete/Person.html', {'Person':diePerson, 'Wettbewerbe':ListeWettbewerbe, 'Teilnahmen':ListeTeilnahmen, 'sTeilnahmen':ListesonstigeTeilnahmen})

def UebersichtSeminar(request, Bezeichnung):
	dasSeminar = get_object_or_404(Seminar, urlbezeichnung=Bezeichnung)
	return render(request, 'Margarete/Seminar.html', {'Seminar':dasSeminar})

def Teilnahmeeintragen(request, urlVeranstaltung):
	dieVeranstaltung = get_object_or_404(Veranstaltung, urlbezeichnung=urlVeranstaltung)
	diePersonen = Person.objects.all()
	#print dieVeranstaltung.bezeichnung
	dieTeilnahmekonzepte = []
	try:
		dieVeranstaltung.wettbewerbsveranstaltung
	except Wettbewerbsveranstaltung.DoesNotExist:
		try:
			dieVeranstaltung.konkretesseminar
		except KonkretesSeminar.DoesNotExist:
			try:
				dieVeranstaltung.sonstigeveranstaltung
			except SonstigeVeranstaltung.DoesNotExist:
				return render(request, 'Margarete/Teilnahmeeintragen.html', {'Veranstaltung':dieVeranstaltung, 'Personen':diePersonen, 'Teilnahmearten':[], 'error_message':'Es gibt ein Problem mit dieser Veranstaltung. Bitte kontaktiere einen Administrator'})
			else:
				dieTeilnahmekonzepte = Teilnahmekonzept.objects.filter(sonstigeveranstaltung__veranstaltung_ptr=dieVeranstaltung)#dieVeranstaltung.teilnahmearten
		else:
			dieTeilnahmekonzepte = Teilnahmekonzept.objects.filter(seminar__konkretesseminar__veranstaltung_ptr=dieVeranstaltung)#dieVeranstaltung.seminar.teilnahmearten
	else:
		dieTeilnahmekonzepte = Teilnahmekonzept.objects.filter(wettbewerbsrunde__konkretewettbewerbsrunde__wettbewerbsveranstaltung__veranstaltung_ptr=dieVeranstaltung)#dieVeranstaltung.wettbewerbsveranstaltung.konkreteWettbewerbsrunde.wettbewerbsrunde.teilnahmearten
	dieTeilnahmearten = []
	for teilnahmekonzept in dieTeilnahmekonzepte:
		dieTeilnahmearten += ArtTeilnahme.objects.filter(teilnahmekonzept=teilnahmekonzept)#teilnahmekonzept.teilnahmearten
	list(set(dieTeilnahmearten))
	return render(request, 'Margarete/Teilnahmeeintragen.html', {'Veranstaltung':dieVeranstaltung, 'Personen':diePersonen, 'Teilnahmearten':dieTeilnahmearten})

def Teilnahmeeintragensubmit(request, Bezeichnung):
	dieVeranstaltung = get_object_or_404(Veranstaltung, urlbezeichnung=Bezeichnung)
	try:
		diePerson = Person.objects.get(pk=request.POST['Person'])
		dieTeilnahmeart = ArtTeilnahme.objects.get(pk=request.POST['Teilnahmeart'])
	except (KeyError,Person.DoesNotExist,ArtTeilnahme.DoesNotExist):
		return render(request, 'Margarete/Teilnahmeeintragen.html', {'question': question, 'error_message': "Bitte wähle etwas aus!"})
	else:
		try:
			t = Teilnahme.objects.get(person=diePerson,veranstaltung=dieVeranstaltung)
		except Teilnahme.DoesNotExist:
			t = Teilnahme(person=diePerson,veranstaltung=dieVeranstaltung,teilnahmeart=dieTeilnahmeart)
		else:
			t.teilnahmeart=dieTeilnahmeart
		t.save()
		return HttpResponseRedirect(reverse('Margarete:Veranstaltung',args=(Bezeichnung,)))

def UebersichtVeranstaltungen(request):
	Veranstaltungen = Veranstaltung.objects.all().order_by('-erstelldatum')
	return render(request, 'Margarete/Veranstaltungen.html', {'Veranstaltungen':Veranstaltungen})