from django import forms
from investor.models import Investor
from accounts.models import User
from django.contrib.auth.forms import UserCreationForm


class AddBalanceForm(forms.Form):
    name = forms.CharField(label='name', required =True, widget=forms.TextInput(attrs={'placeholder':'Enter your name...'}))
    address = forms.CharField(label='address', required =True, widget=forms.TextInput(attrs={'placeholder':'Enter your address...'}))
    amount = forms.IntegerField(label='amount',required=True, widget=forms.NumberInput(attrs={'placeholder':'Ingresa cantidad...', 'class': 'price-box'}))
    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount<=0:
            raise forms.ValidationError('The amount must be greater than zero')
        return amount

class InvestorCreationForm(UserCreationForm):
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
        widgets = {'email':forms.EmailInput(
            attrs={'placeholder': 'Email...',
            }),
            'first_name':forms.TextInput(attrs={'placeholder': 'Name...'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Last name...'}),
            'username':forms.TextInput(attrs={'placeholder': 'Username...'}),
        }   
    def clean_username(self):
        username = self.cleaned_data["username"]
        if User.objects.filter(username = username).exists():
            raise forms.ValidationError('The username is not available')
        return username

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('The email is not available')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Contraseñas no coinciden!')
        return password2
    

    def save(self):
        user = User.objects.create_user(self.cleaned_data['username'], self.cleaned_data['email']) 
        user.last_name = self.cleaned_data['last_name']
        user.first_name = self.cleaned_data['first_name']
        user.user_investor = True
        user.set_password(self.cleaned_data['password1'])
        user.save()
        data = {
            'user': user,
        }
        investor = Investor.objects.create(**data)
        investor.save()