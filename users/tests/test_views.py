from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from ..models import User


class ViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        
        self.login_url = reverse('login')
        self.home_url = reverse('home')
        self.register_url = reverse('register')
        self.register_validation_url = reverse('validation')
        self.login_validation_url = reverse('login_validation')
        
        self.username = 'testuser'
        self.email = 'test@gmail.com'
        self.password = '1234!@#$qweR'
        
        self.user = User.objects.create_user(
            username=self.username,
            email=self.email,
            password=self.password
        )
    
    def test_register_success(self):
        response = self.client.post(
            path=reverse('validation'),
            data={
                'name': 'Caio',
                'email': 'caio@gmail.com',
                'password': '1234!@#$qweR'
            },
            follow=True
        )
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='Caio').exists())

    def test_register_invalid_credentials(self):
        response = self.client.post(
            path=reverse('validation'),
            data={
                'name': 'Caio',
                'email': 'caio@gmail.com',
                'password': '1234'
            },
            follow=True
        )
        self.assertRedirects(response, self.register_url)

    def test_login_success(self):
        response = self.client.post(
            path = self.login_validation_url,
            data = {
                'username': self.username,
                'password': self.password
            },
            follow=True
        )
        self.assertRedirects(response, self.home_url)

    def test_login_invalid_credentials(self):
        response = self.client.post(
            path=self.login_validation_url,
            data = {
                'username': 'invaliduser',
                'password': 'invalidpassword'
            },
            follow=True
        )
        self.assertRedirects(response, self.login_url)
