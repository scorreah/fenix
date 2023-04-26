from django.shortcuts import render,  redirect
from django.contrib.auth import authenticate, login
from .forms import ProjectOwnerCreationForm


def create_project_owner(request):
    if request.method == 'POST':
        form = ProjectOwnerCreationForm(request.POST)
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
        form = ProjectOwnerCreationForm()
    return render(request, 'create_project_owner.html', {'form': form})

