# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ggg(models.Model):
    urlbezeichnung = models.SlugField(max_length=20, null=True, blank=True)
    bezeichnung = models.CharField(max_length=60)
    erstelldatum = models.DateTimeField(auto_now_add=True)
    beschreibung = models.CharField(max_length=500, null=True, blank=True)
    def __str__(self):
        return str(self.urlbezeichnung)

    class Meta:
        abstract = True


class Fachbereich(ggg):
    '''z.B.: Mathematik, Physik'''
    pass
	#self.delattr('beschreibung')

class ArtTeilnahme(ggg):
    '''z.B.: 1.Preis, Bronze, Teilname, Betreuer'''
    wert = models.IntegerField(null=True, blank=True)
	#self.delattr('beschreibung')

class Teilnahmekonzept(ggg):
    '''z.B.: 1.,2.,3. Preis, Medallien, Anerkennungspreis, Teilnahme, Korrektor, Betreuer'''
    teilnahmearten = models.ManyToManyField(ArtTeilnahme)
	#self.delattr('beschreibung')

class Person(ggg):
    '''z.B. Margarete, Max'''
    vorname = models.CharField(max_length=60)
    nachname = models.CharField(max_length=60)
	#self.delattr('beschreibung')
    user = models.OneToOneField(User, on_delete=models.SET_NULL,null=True, blank=True)

class Wettbewerb(ggg):
    '''z.B.: Mathematik-Olympiade, IPhO, Bundeswettbewerb Mathematik'''
    fachbereich = models.ForeignKey(Fachbereich, on_delete=models.SET_NULL,null=True)

class Veranstaltung(ggg):
    '''z.B.: Physik-Seminar Rietschen, 3. Runde der 47. IPhO, Landesrunde Sachsen 55. Mathematik-Olympiade'''
    ort = models.CharField(max_length=20, blank=True, null=True)
    zeitBeginn = models.DateField(verbose_name='Zeitpunkt vom Beginn der Veranstaltung', null=True, blank=True)
    zeitEnde = models.DateField(verbose_name='Zeitpunkt vom Ende der Veranstaltung', null=True, blank=True)
    fachbereich = models.ForeignKey(Fachbereich, on_delete=models.SET_NULL,null=True,blank=True)
    teilnehmer = models.ManyToManyField(Person, through='Teilnahme')

class Teilnahme(models.Model):
    person = models.ForeignKey(Person, on_delete=models.SET_NULL,null=True)
    veranstaltung = models.ForeignKey(Veranstaltung, on_delete=models.SET_NULL,null=True)
    teilnahmeart = models.ForeignKey(ArtTeilnahme, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return self.person.__str__() + '-' + self.veranstaltung.__str__()


class Wettbewerbsrunde(ggg):
    '''z.B.: IPhO 4.Runde, Landesrunde der Mathematik-Olympiade (3.Stufe)'''
    runde = models.IntegerField()
    wettbewerb = models.ForeignKey(Wettbewerb, on_delete=models.SET_NULL,null=True)
    teilnahmearten = models.ManyToManyField(Teilnahmekonzept)
    def __str__(self):
        return self.wettbewerb.__str__() + ' - Runde ' + str(self.runde)
    
class KonkreteWettbewerbsrunde(ggg):
    '''z.B.: 3. Runde der 47. IPhO, Landesrunde der 55. Mathematik-Olympiade'''
    nummer = models.IntegerField(default=1)
    jahr = models.IntegerField(null=True,blank=True)
    wettbewerbsrunde = models.ForeignKey(Wettbewerbsrunde, on_delete=models.SET_NULL,null=True)
    def __str__(self):
        return str(self.nummer) + '. ' + self.wettbewerbsrunde.__str__()

class Wettbewerbsveranstaltung(Veranstaltung):
    '''z.B. 3. Runde der 47. IPhO in Goettingen, Landesrunde der 55. Mathematik-Olympiade von Sachsen'''
    konkreteWettbewerbsrunde = models.ForeignKey(KonkreteWettbewerbsrunde, on_delete=models.SET_NULL,null=True)

class Seminar(ggg):
    '''Dazu zählen alle Veranstaltungen die regelmäßig stattfinden sollen (meist jährlich)
    oder Veranstaltungen von denen geplant ist, dass sie mehrfach mit demselben oder einem
    ähnlichen Konzept stattfinden
    z.B. Rietschen-Seminar, Orpheus-Seminar, LSGM-Mathecamp'''
    fachbereich = models.ForeignKey(Fachbereich, on_delete=models.SET_NULL,null=True,blank=True)
    teilnahmearten = models.ManyToManyField(Teilnahmekonzept)
    gehoertzuwettbewerbsrunde = models.ForeignKey(Wettbewerbsrunde, on_delete=models.SET_NULL,null=True,blank=True)
    #z.B. Landesseminar Mathematik Sachsen gehört zu 3. Runde Mathematikolympiade

class KonkretesSeminar(Veranstaltung):
    '''z.B. Rietschen-Seminar 2016, Orpheus-Seminar 2015'''
    seminar = models.ForeignKey(Seminar, on_delete=models.SET_NULL,null=True)
    nummer = models.IntegerField(default=1)
    jahr = models.IntegerField(null=True,blank=True)
    def __str__(self):
        return str(self.nummer) + '. ' + self.seminar.__str__()

class SonstigeVeranstaltung(Veranstaltung):
    '''einmalige Veranstaltungen z.B. Nachtreffen, Party'''
    teilnahmearten = models.ManyToManyField(Teilnahmekonzept)
    istNachtreffenVon = models.ForeignKey(Veranstaltung,on_delete=models.SET_NULL,null=True,blank=True,related_name='nachtreffen')



    



