from django import forms
from django.contrib.auth.forms import AuthenticationForm

from user.models import User

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['type'] = 'text'
        #self.fields['username'].widget.attrs['placeholder']='Nombre de usuario'
        self.fields['password'].widget.attrs['type'] = 'password'
        #self.fields['password'].widget.attrs['placeholder']='Contraseña'