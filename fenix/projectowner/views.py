from django.shortcuts import render
from .forms import ProjectOwnerCreationForm

def create_project_owner(request):
    if request.method == 'POST':
        form = ProjectOwnerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # redirect to success page
    else:
        form = ProjectOwnerCreationForm()
    return render(request, 'create_project_owner.html', {'form': form})

