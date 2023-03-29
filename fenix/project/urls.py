from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects'),
    path('<int:project_id>/', views.detail, name='projects.detail'),
    path('create/', views.create_project, name='projects.create_project'),
]