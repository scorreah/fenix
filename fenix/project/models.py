from django.db.models import Sum
from django.db import models
from projectowner.models import ProjectOwner
from investor.models import Investing
from django.utils import timezone
from investor.models import Investor

class Project(models.Model):
    DEFAULT = 'NON'
    TECHNOLOGY = 'TEC'
    SCIENCE = 'SCI'
    ART = 'ART'
    READING = 'REA'
    HEALTH = 'HEA'
    MUSIC = 'MUS'
    CATEGORY_CHOICES = [
        (DEFAULT, '--Elige una--'),
        (TECHNOLOGY, 'Tecnología'),
        (SCIENCE, 'Ciencia'),
        (ART, 'Arte'),
        (READING, 'Lectura'),
        (HEALTH, 'Salud'),
        (MUSIC, 'Música'),
    ]

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
    category = models.CharField(max_length=3, choices=CATEGORY_CHOICES)

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
    
    def my_investors(self):
        investments = Investing.objects.filter(project=self.id)
        # investors = [i.investor for i in investments]
        repeat_investors = []
        investors= []
        for i in investments:
            invest = {'investor':i.investor,'amount':i.amount,'id':i.id}
            repeat_investors.append(invest)
        for i in repeat_investors:
            for j in repeat_investors[1:]:
                if i['investor'] == j['investor'] and i['id'] != j['id']:
                    i['amount'] = i['amount'] + j['amount']
                    repeat_investors.remove(j)
            investors.append(i)
        return investors
    
    def count_investments(self):
        investments = Investing.objects.filter(project=self.id)
        return investments.count()
    
    def remaining_time(self):
        today = timezone.now().date()
        remaining_days = (self.end_date - today).days
        if (remaining_days < 0):
            return 0
        else:
            return remaining_days

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'