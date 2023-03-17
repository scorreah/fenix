from django.db import models
from django.contrib.auth.models import User


class Investment(models.Model):
    #investor = models.ForeignKey(User, on_delete=models.CASCADE)
    #project = models.ForeignKey(Project, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.investor} invested {self.amount} in {self.project}"
