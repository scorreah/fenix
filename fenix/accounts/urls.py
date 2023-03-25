from django.urls import path
from projectowner.views import create_project_owner
from . import views

urlpatterns = [
    path('project_owner/create', create_project_owner, name='project_owner.login'),
]