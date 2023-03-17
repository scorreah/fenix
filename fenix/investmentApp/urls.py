from django.urls import path
from . import views


urlpatterns = [
    path('', views.investment_list, name='investment_list'),
    path('<int:pk>/', views.investment_detail, name='investment_detail'),
]