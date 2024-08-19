from django.contrib.auth.models import User
from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

def authenticate_user(request):
    jwt_auth = JWTAuthentication()
    try:
        # Attempt to authenticate the user
        user, jwt_value = jwt_auth.authenticate(request)
        if user is not None:
            # If authentication is successful, return the user
            return user
        else:
            # If authentication fails, return None
            return None
    except (TokenError, InvalidToken):
        # If the token is invalid or expired, return None
        return None

class AccessTokenPermission(BasePermission):
    def has_permission(self, request, view):
        # Use the authenticate_user function to authenticate the access_token
        user = authenticate_user(request)
        if user is not None:
            # If authentication is successful, return True
            return True
        else:
            # If authentication fails, return False
            return False

class UserPermission(BasePermission):
    def has_permission(self, request, view):
        # Use the authenticate_user function to authenticate the user
        user = authenticate_user(request)
        if user is not None and not user.is_staff:
            # If the user is a regular user, return True
            return True
        return False

class AdminPermission(BasePermission):
    def has_permission(self, request, view):
        # Use the authenticate_user function to authenticate the user
        user = authenticate_user(request)
        if user is not None and user.is_staff:
            # If the user is an admin, return True
            return True
        return False