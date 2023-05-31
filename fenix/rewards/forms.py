from django import forms
from .models import Reward

class RewardForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    money_from = forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Monto'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Descripción'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'placeholder': 'Imagen'}))

    class Meta:
        model = Reward
        fields = ['name', 'money_from', 'description', 'image']
