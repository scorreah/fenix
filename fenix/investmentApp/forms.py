from django import forms
from .models import Investment


class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ('amount',)
        widgets = {
            'amount': forms.NumberInput(attrs={'step': '0.01'}),
        }