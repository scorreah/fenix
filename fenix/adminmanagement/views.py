from django.shortcuts import render
from project.models import Project
from django.shortcuts import get_object_or_404, redirect

def home(request):
    if (request.user.is_authenticated and request.user.is_staff):
        projects = Project.objects.all()
        return render(request, 'admin_home.html',{'projects': projects})
    else: 
        return render(request,'unauthorized.html')

def accept(request,project_id):
    project = get_object_or_404(Project,pk=project_id)
    if (request.user.is_authenticated and request.user.is_staff):
        if(project.is_approved == 0):
            project.is_approved = 1
            project.save()
        projects = Project.objects.all()
        return render(request,'admin_home.html',{'projects': projects})
    else:
        return render(request,'unauthorized.html')
