from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from products.models import Product
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class TestProductListView(APITestCase):
    def setUp(self):
        # Setup a user for authentication
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        # Assuming you need an authenticated user for this operation
        refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {refresh.access_token}')

        # Create some product instances to test with
        Product.objects.create(name="Product1", description="Description1", price=100)
        Product.objects.create(name="Product2", description="Description2", price=200)

    def test_list_products(self):
        """
        Ensure we can retrieve a list of products.
        """
        url = reverse('product-list')  # Adjust the name based on your actual URL name
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # We expect two products to be returned

    def tearDown(self):
        # Clean up any objects if necessary
        self.user.delete()
        Product.objects.all().delete()
