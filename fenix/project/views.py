from django.shortcuts import render
from .models import Project
from rewards.models import Reward
from accounts.models import User
from projectowner.models import ProjectOwner
from .forms import FormProject, DoInvestmentForm
from rewards.forms import RewardForm
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages

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
                  {'project':project, 'project_id':project_id})
    
def edit(request, project_id):
    try:
        project = Project.objects.get(id=project_id)
    except Project.DoesNotExist:
        return redirect('projects')

    if project.owner.user != request.user:
        return redirect('projects')

    return render(request, 'project_edit.html', {'project': project})

def create_reward(request, project_id):
    project = Project.objects.get(pk=project_id)

    if request.user != project.owner.user:
        return redirect('projects')

    if request.method == 'POST':
        form = RewardForm(request.POST, request.FILES)
        if form.is_valid():
            reward = form.save(commit=False)
            reward.project = project
            reward.save()
            return redirect('projects.my_projects')
    else:
        form = RewardForm()

    return render(request, 'create_reward.html', {'form': form, 'project': project})

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

def myprojects(request):
    user = User.objects.get(username =request.user)
    if (user.user_project_owner == True):
        project_owner = ProjectOwner.objects.get(user=request.user)
        # Filtrar los proyectos por la instancia del modelo ProjectOwner
        projects = Project.objects.filter(owner=project_owner)
        return render(request, 'my_projects.html', {'projects': projects})
    else:
        return redirect('projects')
    
def myinvestors(request, project_id):
    project = Project.objects.get(id=project_id)
    investors = project.my_investors()
    return render(request, 'investor_details.html', {'investors': investors})

def invest(request, project_id):
    project = get_object_or_404(Project,pk=project_id)
    rewards = Reward.objects.filter(project=project)
    if request.method == 'POST':
        form = DoInvestmentForm(request.POST)
        if form.is_valid():
            if request.user.user_investor:
                investor = User.objects.get(username = request.user)
                if form.save(investor, project_id):
                    messages.success(request, "La inversion ha sido realizada con exito")
                else:
                    messages.error(request, "No tienes fondos suficientes")
            else:
                messages.error(request, "El usuario no es un inversor")
        return redirect('projects.detail', project_id=project_id)
    else:
        form = DoInvestmentForm()
        return render(request, 'project_invest.html', 
                  {'form': form, 'project':project, 'project_id':project_id, 'rewards':rewards})
    
    
