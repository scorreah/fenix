from django.urls import path
from projectowner.views import create_project_owner
from investor.views import create_investor
from . import views

urlpatterns = [
    path('project_owner/create', create_project_owner, name='project_owner.singup'),
    path('investor/create', create_investor, name='investor.singup'),
]