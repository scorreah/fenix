from django.test import TestCase
from django.utils import timezone
from projectowner.models import ProjectOwner
from accounts.models import User
from investor.models import Investing, Investor
from .models import Project

class ProjectModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='sochoac', first_name='Santy', last_name='Ochoa', user_project_owner=True)
        self.user2 = User.objects.create(username='miguel', first_name='Miguelito', last_name='Zapata', user_project_owner=True)
        self.owner = ProjectOwner.objects.create(user=self.user)
        self.project = Project.objects.create(
            title='Test Project',
            description='Test Description',
            goal_amount=1000.00,
            current_amount=0.00,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=30),
            owner=self.owner,
            category=Project.TECHNOLOGY,
        )

    def test_project_creation(self):
        self.assertIsInstance(self.project, Project)
        self.assertEqual(self.project.title, 'Test Project')
        self.assertEqual(self.project.description, 'Test Description')
        self.assertEqual(self.project.goal_amount, 1000.00)
        self.assertEqual(self.project.current_amount, 0.00)
        self.assertEqual(self.project.owner, self.owner)
        self.assertEqual(self.project.category, Project.TECHNOLOGY)

    def test_get_is_approved(self):
        self.assertFalse(self.project.get_is_approved())

    def test_get_title(self):
        self.assertEqual(self.project.get_title(), 'Test Project')

    def test_get_description(self):
        self.assertEqual(self.project.get_description(), 'Test Description')

    def test_get_goal_amount(self):
        self.assertEqual(self.project.get_goal_amount(), 1000.00)

    def test_my_investors(self):
        investor1 = Investor.objects.create(user=self.user, balance=5000000)
        investor2 = Investor.objects.create(user=self.user2, balance=5000000)
        Investing.objects.create(
            project=self.project.id,
            investor=investor1,
            amount=500.00,
        )
        Investing.objects.create(
            project=self.project.id,
            investor=investor2,
            amount=1000.00,
        )
        investors = self.project.my_investors()
        self.assertTrue(any(invest['investor'] == investor1 for invest in investors))
        self.assertTrue(any(invest['investor'] == investor2 for invest in investors))
