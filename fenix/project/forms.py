from django import forms
from django.contrib.auth.models import Group
from .models import Project
from investor.models import Investor
from accounts.models import User
from investor.models import Investing

from .models import Project

class DateInput(forms.DateInput):
    input_type = 'date'

class FormProject(forms.Form):
    title = forms.CharField(label='title', required =True, widget=forms.TextInput(attrs={'placeholder':'Enter the project title...'}))
    description = forms.CharField(label='description',required=True, widget=forms.TextInput(attrs={'placeholder':'Enter the project description...'}))
    goal_amount = forms.IntegerField(label='goal_amount',required=True, widget=forms.NumberInput(attrs={'placeholder':'Enter the goal amount..'}))
    start_date = forms.DateField(label='start_date', required=True, widget=DateInput)
    end_date = forms.DateField(label='end_date', required=True, widget=DateInput)
    image = forms.ImageField(label='image')

    def clean_goal_amount(self):
        goal_amount = self.cleaned_data['goal_amount']
        if goal_amount<=0:
            raise forms.ValidationError('The goal amount must be greater than zero')
        return goal_amount

    def clean_end_date(self):
        end_date = self.cleaned_data['end_date']
        if end_date<self.cleaned_data['start_date']:
            raise forms.ValidationError('The end date must be greater than the start date')
        return end_date
    
    def clean_title(self):
        title = self.cleaned_data['title']
        projects_with_title = Project.objects.filter(title=title)

        if projects_with_title.exists():
            raise forms.ValidationError("Already exist a project with this title.")
        else:
            return title
    
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

class DoInvestmentForm(forms.Form):
    amount = forms.IntegerField(label='amount',required=True, widget=forms.NumberInput(attrs={'placeholder':'Enter the amount..'}))

    def clean_amount(self):
        amount = self.cleaned_data['amount']
        if amount<=0:
            raise forms.ValidationError('The amount must be greater than zero')
        return amount
    
    def save(self, investor, project_id):
        investor = Investor.objects.get(user=investor)
        data_clean = self.cleaned_data
        if investor.balance - data_clean['amount']<0:
            return False     
        investor.balance = investor.balance - data_clean['amount']
        investor.save()  
        project = Project.objects.get(id=project_id)
        project.current_amount += data_clean['amount']
        project.save()
        data_clean = self.cleaned_data
        data = {
            'investor': investor,
            'amount' : data_clean['amount'],
            'project' : project_id
        }
        Investing.objects.create(**data)
