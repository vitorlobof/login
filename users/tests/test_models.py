from django.test import TestCase
from ..models import User


class UserTestCase(TestCase):
    def setUp(self):
        self.username = 'caio'
        self.email = 'caio@gmail.com'
        self.password = '1234'
        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )
    
    def test_user_was_saved_in_db(self):
        self.assertTrue(User.objects.filter(username=self.username).exists())
    
    def test_password_was_hashed(self):
        self.assertNotEqual(self.password, self.user.password)
        self.assertEqual(len(self.user.password), 88)
