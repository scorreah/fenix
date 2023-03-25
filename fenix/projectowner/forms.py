from django import forms
from projectowner.models import ProjectOwner
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class ProjectOwnerCreationForm(UserCreationForm):
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Password...',
            'id':'password1',
            'required':'required',
        }
    ))

    password2 = forms.CharField(label='password2', widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Confirm password...',
            'id':'password2',
            'required':'required',
        }
    ))

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email', 'password1', 'password2']
    
    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('The username is not available')
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2

    def save(self, commit=True):
        user = super(ProjectOwnerCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.user_project_owner = True
        user.save()
        project_owner = ProjectOwner.objects.create(user=user)
        if commit:
            project_owner.save()
        return project_owner
