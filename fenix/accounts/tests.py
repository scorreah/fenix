from django.test import TestCase
from django.contrib.auth import get_user_model

class UserTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create(
            username='testuser',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            user_investor=True,
            user_project_owner=False
        )

    def test_user_creation(self):
        self.assertIsInstance(self.user, get_user_model())
        self.assertEqual(self.user.username, 'testuser')
        self.assertEqual(self.user.first_name, 'Test')
        self.assertEqual(self.user.last_name, 'User')
        self.assertEqual(self.user.email, 'testuser@example.com')
        self.assertEqual(self.user.user_investor, True)
        self.assertEqual(self.user.user_project_owner, False)

    def test_get_investor(self):
        self.assertEqual(self.user.get_investor(), True)

    def test_get_project_owner(self):
        self.assertEqual(self.user.get_project_owner(), False)
