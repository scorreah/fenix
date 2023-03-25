from django.db import models
from accounts.models import User

class Investor(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=1000000)
    
    class Meta:
        verbose_name = 'Investor'
        verbose_name_plural = 'Investors'