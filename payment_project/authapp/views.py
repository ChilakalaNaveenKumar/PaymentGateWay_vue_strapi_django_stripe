import stripe
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework_simplejwt.views import TokenObtainPairView
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data['access']

        # Create a secure HttpOnly cookie to store the token
        response.set_cookie(
            key='jwt_token',
            value=token,
            httponly=True,
            secure=False,  # Set to True in production with HTTPS
            samesite='Lax',
            max_age=3600,  # 1 hour expiration
            domain=settings.SESSION_COOKIE_DOMAIN,  # Shared across subdomains if needed
        )
        return response

# Serializer for user registration
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        
    def validate(self, data):
        if 'username' not in data or 'password' not in data:
            raise serializers.ValidationError("Username and password are required")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user

# View to handle user registration
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ForgotPasswordView(APIView):
    def post(self, request):
        # Here, add logic to reset password (e.g., send email)
        email = request.data.get('email')
        # Simulate email sending
        return Response({"message": "Password reset link sent!"}, status=status.HTTP_200_OK)

# Stripe API Key (add this to your settings.py file)
stripe.api_key = "your_publishable_stripe_key"

class StripePaymentView(APIView):
    def post(self, request):
        try:
            # Get the amount from the frontend, e.g., $10 -> 1000 (Stripe works with cents)
            amount = request.data.get('amount')

            # Create PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=int(amount),
                currency='usd',
                payment_method_types=['card'],
            )
            return Response({"clientSecret": intent['client_secret']}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ProductSuggestionsView(APIView):
    def get(self, request):
        # Imagine this list is fetched from the database or a machine learning model
        products = [
            {"id": 1, "name": "Product A", "price": 100},
            {"id": 2, "name": "Product B", "price": 150},
            {"id": 3, "name": "Product C", "price": 200},
        ]

        # Business logic to suggest products based on request data (e.g., user preferences)
        # Here, we're simply returning all products for demo purposes.
        return Response(products, status=status.HTTP_200_OK)
