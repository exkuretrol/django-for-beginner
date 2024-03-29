from django.contrib.auth import get_user_model
from django.test import TestCase


class UserManagerTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            email="test@kuaz.info",
            password="testpass",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "test@kuaz.info")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
    
    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="testadmin",
            email="testadmin@kuaz.info",
            password="testpass",
        )
        self.assertEqual(user.username, "testadmin")
        self.assertEqual(user.email, "testadmin@kuaz.info")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
