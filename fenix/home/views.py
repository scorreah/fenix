from django.shortcuts import render
from project.models import Project
from investor.models import Investing
from accounts.models import User
from django.db.models import Sum

def home(request):
    total_investor = User.objects.filter(user_investor=True).count()
    total_projects = Project.objects.all().count()
    global_amount_invested = Investing.objects.all().aggregate(Sum('amount'))
    investments = Investing.objects.all()
    repeat_investors = []
    investors = []
    for i in investments:
        invest = {'investor':i.investor,'amount':i.amount, 'id':i.id}
        repeat_investors.append(invest)
    for i in repeat_investors:
        for j in repeat_investors[1:]:
            if i['investor'] == j['investor'] and i['id'] != j['id']:
                repeat_investors.remove(j)
        investors.append(i)
    global_statistics = {'total_investor':total_investor,'real_investor': len(investors),'global_amount_invested':global_amount_invested['amount__sum'],'total_projects':total_projects}
    return render(request, 'home.html',{'global_statistics':global_statistics})