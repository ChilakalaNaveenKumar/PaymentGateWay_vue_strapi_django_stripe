from django.utils.deprecation import MiddlewareMixin

class JWTAuthFromCookieMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Check if the JWT token exists in cookies
        token = request.COOKIES.get('jwt_token')
        if token:
            print(token)
            # Add the token to the Authorization header
            request.META['HTTP_AUTHORIZATION'] = f'Bearer {token}'
