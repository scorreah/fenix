from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects'),
    path('<int:project_id>/', views.detail, name='projects.detail'),
    path('invest/<int:project_id>/', views.invest, name='projects.invest'),
    path('create/', views.create_project, name='projects.create_project'),
    path('myprojects/', views.myprojects, name='projects.my_projects'),
    path('myprojects/edit/<int:project_id>/', views.edit, name='projects.my_projects_edit'),
    path('myprojects/investors/<int:project_id>/', views.myinvestors, name='projects.my_investors'),
    path('myprojects/reward/<int:project_id>/', views.create_reward, name='projects.create_reward'),
]