from django.shortcuts import render
from .models import Project
from accounts.models import User
from projectowner.models import ProjectOwner
from .forms import FormProject
from django.shortcuts import get_object_or_404, redirect

def home(request):
    searchTerm = request.GET.get('searchMovie')
    projects = Project.objects.all()
    return render(request, 'project_home.html',
      {'searchTerm':searchTerm, 'projects': projects})


def detail(request, project_id):
    project = get_object_or_404(Project,pk=project_id)
    return render(request, 'project_detail.html', 
                  {'project':project})

def create_project(request):
    user = User.objects.get(username =request.user)
    if (user.user_project_owner == False):
        return redirect('home')
    project_owner = ProjectOwner.objects.get(user = user)

    if request.method == 'POST':
        form = FormProject(request.POST)
        if form.is_valid():
            form.create(project_owner)
    else:
        form = FormProject()
    return render(request, 'project_create.html', {'form':form})
