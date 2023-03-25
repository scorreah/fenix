from django.db import models
from accounts.models import User

class ProjectOwner(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Project owner'
        verbose_name_plural = 'Project owners'