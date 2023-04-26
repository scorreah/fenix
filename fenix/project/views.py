from django.shortcuts import render
from .models import Project
from accounts.models import User
from projectowner.models import ProjectOwner
from .forms import FormProject
from django.shortcuts import get_object_or_404, redirect

def home(request):
    projects = Project.objects.all()
    category = request.GET.get('category')
    # Verificar si se ha enviado el formulario de filtro
    if category:
        # Filtrar los proyectos según la categoría seleccionada
        
        projects = projects.filter(category=category)

    return render(request, 'project_home.html',
    {'projects': projects, 'category':category})


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
        form = FormProject(request.POST, request.FILES)
        if form.is_valid():
            form.create(project_owner)
            projects = Project.objects.all()
            return render(request, 'project_home.html', {'projects':projects})
    else:
        form = FormProject()
    return render(request, 'project_create.html', {'form':form})
