from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import User

class AuthTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        data = {
            "firstName": "Hng",
            "lastName": "Backend",
            "email": "hngbackendtrack@example.com",
            "password": "hng112024",
            "phone": "2468101214"
        }
        response = self.client.post('/auth/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('accessToken', response.data['data'])
        self.assertEqual(response.data['data']['user']['email'], data['email'])

    def test_login_user(self):
        user = User.objects.create_user(email='john@example.com', first_name='John', last_name='Doe', password='pass1234')
        data = {
            "email": "hngbackendtrack@example.com",
            "phone": "2468101214"
        }
        response = self.client.post('/auth/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('accessToken', response.data['data'])
        self.assertEqual(response.data['data']['user']['email'], data['email'])

    def test_register_user_missing_fields(self):
        data = {
            "firstName": "hng",
            "email": "hngbackendtrack@example.com",
            "phone": "2468101214"
        }
        response = self.client.post('/auth/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.data['errors'][0]['field'], 'lastName')

    def test_register_duplicate_email(self):
        User.objects.create_user(email='john@example.com', first_name='John', last_name='Doe', password='pass1234')
        data = {
            "firstName": "Hng",
            "lastName": "Backend",
            "email": "hngbackendtrack@example.com",
            "password": "hng112024",
            "phone": "2468101214"
        }
        response = self.client.post('/auth/register/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_422_UNPROCESSABLE_ENTITY)
        self.assertEqual(response.data['errors'][0]['field'], 'email')
