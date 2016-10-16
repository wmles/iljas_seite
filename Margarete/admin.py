from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Fachbereich)
admin.site.register(Wettbewerb)
admin.site.register(Wettbewerbsrunde)
admin.site.register(KonkreteWettbewerbsrunde)
admin.site.register(ArtTeilnahme)
admin.site.register(Teilnahmekonzept)
admin.site.register(Person)
admin.site.register(Wettbewerbsveranstaltung)
admin.site.register(Seminar)
admin.site.register(KonkretesSeminar)
admin.site.register(Teilnahme)
admin.site.register(SonstigeVeranstaltung)
admin.site.register(Veranstaltung)

