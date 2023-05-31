from django.test import TestCase
from django.contrib.auth import get_user_model
from projectowner.models import ProjectOwner

class ProjectOwnerTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='testowner',
            first_name='Test',
            last_name='Owner',
            email='testowner@example.com',
            user_investor=False,
            user_project_owner=True
        )
        self.project_owner = ProjectOwner.objects.create(user=self.user)

    def test_project_owner_creation(self):
        self.assertIsInstance(self.project_owner, ProjectOwner)
        self.assertEqual(self.project_owner.user, self.user)

    def test_project_owner_string_representation(self):
        self.assertEqual(str(self.project_owner), 'testowner')
