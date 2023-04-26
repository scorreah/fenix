from django.shortcuts import render,  redirect
from .forms import InvestorCreationForm
from django.contrib.auth import authenticate, login

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
            # redirect to success page
    else:
        form = InvestorCreationForm()
    return render(request, 'create_investor.html', {'form': form})