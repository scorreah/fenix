from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Investment
from .forms import InvestmentForm


def investment_list(request):
    investments = Investment.objects.all()
    return render(request, 'investmentApp/investment_list.html', {'investments': investments})


def investment_detail(request, pk):
    investment = get_object_or_404(Investment, pk=pk)
    form = InvestmentForm()
    return render(request, 'investmentApp/investment_detail.html', {'investment': investment, 'form': form})
