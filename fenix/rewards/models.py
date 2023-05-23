from django.db import models
from project.models import Project


class Reward(models.Model):
    name = models.CharField(max_length=100)
    money_from = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project/images/', null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
