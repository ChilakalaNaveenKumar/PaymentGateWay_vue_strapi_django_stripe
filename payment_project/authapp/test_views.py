import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

@pytest.mark.django_db
class TestAuthAppViews:
    def setup_method(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', email='test@example.com', password='password123')
        self.user.save()

    def test_user_registration(self):
        """
        Test registering a new user.
        """
        url = reverse('register')  # Adjust with your actual URL name for registration
        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'newpassword123'
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_user_login(self):
        """
        Test user login and token retrieval.
        """
        url = reverse('token_obtain_pair')  # Adjust with your actual token URL
        data = {
            'username': 'testuser',
            'password': 'password123'
        }
        response = self.client.post(url, data)
        assert response.status_code == status.HTTP_200_OK
        assert 'access' in response.data
        assert 'refresh' in response.data

    def teardown_method(self):
        self.user.delete()
