from django.contrib.auth import get_user_model
from django.core.validators import validate_email


class EmailAuthBackend(object):
    """
    Аутентификация по e-mail.
    """

    def __init__(self):
        self.CurUserModel = get_user_model()

    def authenticate(self, username=None, password=None):
        if validate_email.search(username):
            try:
                user = self.CurUserModel.objects.get(email=username)
            except self.CurUserModel.DoesNotExist:
                return None
        else:
            try:
                user = self.CurUserModel.objects.get(username=username)
            except self.CurUserModel.DoesNotExist:
                return None
        if user.check_password(password):
            return user

    def get_user(self, user_id):
        try:
            return self.CurUserModel.objects.get(pk=user_id)
        except self.CurUserModel.DoesNotExist:
            return None
