from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from .models import Notizzeile

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Notizzettel/index.html'
    context_object_name = 'ListeZeilen'

    def get_queryset(self):
        """Return the last five published questions."""
        return Notizzeile.objects.order_by('erstelldatum')
        

def Eintragen(request):
    Text, Autor = request.POST['Text'], request.POST['Autor']
    NeueZeile = Notizzeile(text = Text, name_autor = Autor)
    NeueZeile.save()
    return HttpResponseRedirect(reverse('Notizzettel:index'))
    

