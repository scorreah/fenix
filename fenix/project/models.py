
from django.db import models
from projectowner.models import ProjectOwner

class Project(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    goal_amount = models.DecimalField(max_digits=10, decimal_places=2)
    current_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(upload_to='project/images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(ProjectOwner, blank = False, null = False, on_delete=models.CASCADE)    
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_is_approved(self):
        return self.is_approved
    
    def get_title(self):
        return self.title
    
    def get_description(self):
        return self.description
    
    def get_goal_amount(self):
        return self.goal_amount

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'