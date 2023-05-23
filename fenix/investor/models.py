from django.db import models
from accounts.models import User
# from project.models import Project

class Investor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)
    
    class Meta:
        verbose_name = 'Investor'
        verbose_name_plural = 'Investors'

class Investing(models.Model):
    investor = models.ForeignKey(Investor, on_delete=models.CASCADE)
    amount = models.IntegerField()
    project = models.IntegerField()
