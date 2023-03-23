from django.shortcuts import render
from .models import Project
from django.shortcuts import get_object_or_404, redirect

def home(request):
    searchTerm = request.GET.get('searchMovie')
    projects = Project.objects.all()
    return render(request, 'project_index.html',
      {'searchTerm':searchTerm, 'projects': projects})


def detail(request, project_id):
    project = get_object_or_404(Project,pk=project_id)
    return render(request, 'prject_detail.html', 
                  {'project':project})