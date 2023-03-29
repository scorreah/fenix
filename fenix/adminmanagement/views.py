from django.shortcuts import render
from project.models import Project
from django.shortcuts import get_object_or_404, redirect

def home(request):
    projects = Project.objects.all()
    return render(request, 'project_home.html',{'projects': projects})

def detail(request, project_id):
    project = get_object_or_404(Project,pk=project_id)
    return render(request, 'project_detail.html', 
                  {'project':project})