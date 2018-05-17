from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import RegistradoModelForm, ContactForm
from .models import Registrado


def inicio(request):
    titulo = 'Bienvenido'
    if request.user.is_authenticated():
        titulo = 'Bienvenido %s'%(request.user)
    form = RegistradoModelForm(request.POST or None)
    contexto = {
        'titulo': titulo,
        'form': form,
    }
    if form.is_valid():
        instance = form.save(commit = False)
        nombre = form.cleaned_data.get('nombre')
        email = form.cleaned_data.get('email')
        instance.save()
        nombre = nombre.capitalize()
        contexto = {
            'titulo': 'Gracias, %s'%(nombre),
        }
    return render(request, 'inicio.html', contexto)

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get('email')
        form_mensaje = form.cleaned_data.get('mensaje')
        form_nombre = form.cleaned_data.get('nombre')
        subject = 'Promociones.....'
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from]
        email_mensaje = '%s: %s enviado por %s'%(form_nombre, form_mensaje, form_email)
        send_mail(subject,
        email_mensaje,
        email_from,
        email_to,
        fail_silently = True
        )

        #Forma 1.- print (nombre, email, mensaje)

        #Forma 2.- Si hay varios campos
        #for key in form.cleaned_data:
        #   print(key)
        #   print form.cleaned_data.get(key)

        #Forma 3.-
        #for key, value in form.cleaned_data.iteritems()
        #   print key, value

    contexto = {
        'form': form,
    }
    return render(request, 'form.html', contexto)
