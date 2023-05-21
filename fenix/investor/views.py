from django.shortcuts import render,  redirect
from .forms import InvestorCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import User
from .models import Investor
from .models import Investing
from project.models import Project

def create_investor(request):
    if request.method == 'POST':
        form = InvestorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # authenticate and login user
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = InvestorCreationForm()
    return render(request, 'create_investor.html', {'form': form})


def myinvestments(request):
    user = User.objects.get(username =request.user)
    if (user.user_investor == True):
        investor_user = Investor.objects.get(user=request.user)
        investments = Investing.objects.filter(investor=investor_user.id)
        projects = []
        for i in investments:
            invest = {'project':Project.objects.get(id=i.project),'amount':i.amount}
            projects.append(invest)
        for i in projects: 
            for j in projects[1:]:
                if i['project'] == j['project']:
                    i['amount'] = i['amount'] + j['amount']
                    projects.remove(j)
        return render(request,'my_investments.html',{'projects':projects})
    else:
        return redirect('projects')