from django import forms
from django.contrib.auth.forms import UserCreationForm
from accounts.models import User

class UserCreateForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2')