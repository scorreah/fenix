from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='projects.index'),
    path('<int:project_id>', views.detail, name='projects.detail'),
]