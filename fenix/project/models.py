
from django.db import models
from projectowner.models import ProjectOwner
from investor.models import Investor

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='project/images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_owner = models.ForeignKey(ProjectOwner, blank = True, null = True, on_delete=models.CASCADE)
    user_investor = models.ForeignKey(Investor, blank = True, null = True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'