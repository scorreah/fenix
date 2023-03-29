from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='admin_projects.index'),
    path('accept/<str:project_id>/', views.accept, name='accept'),
]