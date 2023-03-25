from django.shortcuts import render
from .forms import InvestorCreationForm

def create_investor(request):
    if request.method == 'POST':
        form = InvestorCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to success page
    else:
        form = InvestorCreationForm()
    return render(request, 'create_investor.html', {'form': form})