from django.urls import path
from projectowner.views import SignUp
from . import views

urlpatterns = [
    path('project_owner/create', SignUp, name='project_owner.login'),
]