from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.db import IntegrityError

from django.contrib.auth.models import User

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'Nutzerverwaltung/index.html'
    context_object_name = 'Liste_der_Nutzer'

    def get_queryset(self):
        """Return the last five published questions."""
        return User.objects.order_by('pk')
        
class ProfilView(generic.DetailView):
    model = User
    template_name = 'Nutzerverwaltung/Profil.html'

def MeinProfilAnzeigen(request):
    return HttpResponseRedirect(reverse('Nutzerverwaltung:Profil', args=(request.user.pk, )))    

def MeinPasswortAendern(request):
    return render(request, 'Nutzerverwaltung/PasswortAendern.html')
    
def Registrieren_Anfordern(request):
    return render(request, 'Nutzerverwaltung/register_Formular.html')
    
def Registrieren_MailSenden(request):
    import string, random
    from django.core.mail import send_mail
    username, email = request.POST['username'], request.POST['email']
    password = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
    try:
        user = User.objects.create_user(username, email, password)
    except IntegrityError: # wenn es den Nutzernamen schon gibt - quick&dirty-Loesung, kann verbessert werden
        return HttpResponseRedirect(reverse('Nutzerverwaltung:index'))
    user.last_name, user.first_name = request.POST['last_name'], request.POST['first_name']
    user.save()
    send_mail('Dein Passwort', 'Willkommen, %s!\nJetzt bist du auch Nutzer der GEHEIMEN Webseite!\nDein Passwort lautet: %s\nDu kannst dich jetzt anmelden und das Passwort aendern\nDanke fuer Dein Interesse an der Seite!\nilja' % (username, password), 'iljasseite@googlemail.com', [email, 'iljasseite@googlemail.com'], fail_silently = False, auth_user = 'iljasseite', auth_password = 'iljailja')
    return HttpResponseRedirect(reverse('Nutzerverwaltung:login'))
    
