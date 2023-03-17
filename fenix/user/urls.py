
# Django
from django.urls import path

# Views
from . import views


urlpatterns = [
    path('login/', views.Login.as_view(), name="login"),
]