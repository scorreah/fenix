from django.conf import settings
from django.shortcuts import render,  redirect
from django.urls import reverse
from .forms import InvestorCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from accounts.models import User
from .models import Investor
from .models import Investing
from project.models import Project
from .forms import AddBalanceForm
from paypal.standard.forms import PayPalPaymentsForm
import uuid

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
        repeat_projects = []
        projects = []
        for i in investments:
            invest = {'project':Project.objects.get(id=i.project),'amount':i.amount, 'id':i.id}
            repeat_projects.append(invest)
        for i in repeat_projects: 
            for j in repeat_projects[1:]:
                if i['project'] == j['project'] and i['id'] != j['id']:
                    i['amount'] = i['amount'] + j['amount']
                    repeat_projects.remove(j)
            projects.append(i)
        return render(request,'my_investments.html',{'projects':projects})
    else:
        return redirect('projects')
    
def addBalance(request):
    if request.method == 'POST':
        form = AddBalanceForm(request.POST)
        if form.is_valid():
            if request.user.user_investor:
                amount = form.cleaned_data['amount']
                return paypalPaymethod(request, amount)
            else:
                messages.error(request, "El usuario no es un inversor")
        return redirect('projects')
    else:
        form = AddBalanceForm()
        response = render(request, 'add_balance.html', 
                  {'form': form})
        response.set_cookie('amount', "0")
        return response

def paypalPaymethod(request, amount):
    # What you want the button to do.
    paypal_dict = {
        "business": settings.PAYPAL_RECEIVER_EMAIL,
        "amount": amount,
        "item_name": "name of the item",
        "invoice": str(uuid.uuid4()),
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('paypal-return')),
        "cancel_return": request.build_absolute_uri(reverse('paypal-cancel')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "amount":amount}
    response  = render(request, "payment.html", context)
    response.set_cookie('amount', amount)
    return response

def paypal_return(request):
    amount = request.COOKIES.get('amount')
    investor_user = Investor.objects.get(user=request.user)
    investor_user.balance = investor_user.balance + int(amount)
    investor_user.save()
    messages.success(request,'You  successfully made a payment request')
    return redirect('addBalance')

def paypal_cancel(request):
    messages.error(request,'You payment request cancelled')
    return redirect('addBalance')

