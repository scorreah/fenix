from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    first_name = models.CharField('first name', max_length=150, blank=True, null=True)
    last_name = models.CharField('last name', max_length=150, blank=True, null=True)
    email = models.EmailField('email address', blank=False, null=False)
    investor = models.BooleanField(default=False)
    project_owner = models.BooleanField(default=False)

    def get_investor(self):
        return self.investor

    def get_project_owner(self):
        return self.project_owner
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'