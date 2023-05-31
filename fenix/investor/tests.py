from django.test import TestCase
from accounts.models import User
from django.contrib.auth import get_user_model
from investor.models import Investing, Investor
from projectowner.models import ProjectOwner
from project.models import Project
from django.utils import timezone

class InvestorModelTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            user_investor=True
        )
        self.investor = Investor.objects.create(
            user=self.user,
            balance=5000
        )

    def test_investor_creation(self):
        self.assertIsInstance(self.investor, Investor)
        self.assertEqual(self.investor.user, self.user)
        self.assertEqual(self.investor.balance, 5000)

class InvestingModelTest(TestCase):
    def setUp(self):
        self.user1 = get_user_model().objects.create(
            username='testuser1',
            first_name='Test',
            last_name='User',
            email='testuser1@example.com',
            user_investor=True
        )
        self.user2 = get_user_model().objects.create(
            username='testuser2',
            first_name='Test',
            last_name='User',
            email='testuser2@example.com',
            user_project_owner=True
        )
        self.investor = Investor.objects.create(user=self.user1, balance=5000)
        self.project_owner = ProjectOwner.objects.create(user=self.user2)
        self.project = Project.objects.create(
            title='Test Project',
            description='Test Description',
            goal_amount=1000.00,
            current_amount=0.00,
            start_date=timezone.now(),
            end_date=timezone.now() + timezone.timedelta(days=30),
            owner=self.project_owner,
            category=Project.TECHNOLOGY,
        )
        self.investing = Investing.objects.create(
            project=self.project.id,
            investor=self.investor,
            amount=500
        )

    def test_investing_creation(self):
        self.assertIsInstance(self.investing, Investing)
        self.assertEqual(self.investing.project, self.project.id)
        self.assertEqual(self.investing.investor, self.investor)
        self.assertEqual(self.investing.amount, 500)
