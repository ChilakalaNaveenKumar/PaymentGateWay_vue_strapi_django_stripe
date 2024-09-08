from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import StripePaymentView, ProductSuggestionsView, RegisterUserView, ForgotPasswordView, CustomTokenObtainPairView

urlpatterns = [
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('stripe-payment/', StripePaymentView.as_view(), name='stripe-payment'),
    path('suggestions/', ProductSuggestionsView.as_view(), name='product-suggestions'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot_password'),
]
