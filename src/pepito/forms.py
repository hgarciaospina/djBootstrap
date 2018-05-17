from django import forms
from .models import Registrado

class RegistradoModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ['nombre', 'email']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_base, proveedor = email.split('@')
        dominio, extension  = proveedor.split('.')
        if not extension == 'edu':
            raise forms.ValidationError('Por favor digite un correo con extension edu')
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre')
        nombre = nombre.lower()
        if not(nombre.isalpha()):
            raise forms.ValidationError('Por favor digite solo caracteres ')
        return nombre

class ContactForm(forms.Form):
    nombre = forms.CharField(max_length = 100)
    email = forms.EmailField()
    mensaje = forms.CharField(widget = forms.Textarea)
