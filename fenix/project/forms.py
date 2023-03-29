from django import forms
from django.contrib.auth.models import Group

from .models import Project

class DateInput(forms.DateInput):
    input_type = 'date'

class FormProject(forms.Form):
    title = forms.CharField(label='title', required =True, widget=forms.TextInput(attrs={'placeholder':'Enter the project title...'}))
    description = forms.CharField(label='description',required=True, widget=forms.TextInput(attrs={'placeholder':'Enter the project description...'}))
    goal_amount = forms.IntegerField(label='goal_amount',required=True, widget=forms.NumberInput(attrs={'placeholder':'Enter the goal amount..'}))
    start_date = forms.DateField(label='start_date', required=True, widget=DateInput)
    end_date = forms.DateField(label='end_date', required=True, widget=DateInput)
    image = forms.ImageField(label='image', required = False)

    def clean_goal_amount(self):
        goal_amount = self.cleaned_data['goal_amount']
        if goal_amount<0:
            raise forms.ValidationError('The goal amount must be greater than zero')
        return goal_amount

    def clean_end_date(self):
        end_date = self.cleaned_data['end_date']
        if end_date<self.cleaned_data['start_date']:
            raise forms.ValidationError('The end date must be greater than the start date')
        return end_date
    
    def create(self, user_owner):
        data_clean = self.cleaned_data
        data ={
            'title' : data_clean['title'],
            'description' : data_clean['description'],
            'goal_amount' : data_clean['goal_amount'],
            'current_amount' : data_clean['goal_amount'],
            'start_date' : data_clean['start_date'],
            'end_date' : data_clean['end_date'],
            'image' : data_clean['image'],
            'owner' : user_owner
        }
        Project.objects.create(**data)