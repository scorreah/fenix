from django.shortcuts import render, redirect
from .forms import UserCreateForm

def SignUp(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'project_owner_login.html', {'form': form})
    else:
        form = UserCreateForm()
    return render(request, 'project_owner_login.html', {'form': form})
