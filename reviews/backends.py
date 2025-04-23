from django.contrib.auth.backends import ModelBackend
from .models import UserRegister

class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = UserRegister.objects.get(username=username)
            if user.check_password(password):
                return user
        except UserRegister.DoesNotExist:
            print('Unable to authenticate')
            return None
    def get_user(self, user_id):
        try:
            return UserRegister.objects.get(pk=user_id)
        except UserRegister.DoesNotExist:
            return None