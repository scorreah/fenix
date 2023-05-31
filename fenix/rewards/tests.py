from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from projectowner.models import ProjectOwner
from project.models import Project
from rewards.models import Reward

class RewardTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='testowner',
            first_name='Test',
            last_name='Owner',
            email='testowner@example.com',
            user_project_owner=True
        )
        self.project_owner = ProjectOwner.objects.create(user=self.user)
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
        self.reward = Reward.objects.create(
            name='Test Reward',
            money_from='100',
            description='Test Description',
            project=self.project,
        )

    def test_reward_creation(self):
        self.assertIsInstance(self.reward, Reward)
        self.assertEqual(self.reward.project, self.project)

    def test_reward_string_representation(self):
        self.assertEqual(str(self.reward), 'Test Reward')
