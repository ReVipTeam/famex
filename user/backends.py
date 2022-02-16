from django.contrib.auth.backends import BaseBackend
from .models import User


class Backend(BaseBackend):

    def authenticate(self, request, username=None, password=None):
        user = User.objects.get(username=username)
        if user.password == password:
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
