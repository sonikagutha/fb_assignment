from fb_auth.models import User
from django.utils import timezone
from fb_auth.interactor.storage_interfaces.register_user_storage import RegisterUserStorageInterface
class RegisterUserStorage(RegisterUserStorageInterface):
    def register_user(self, username, password, access_token, token_created_at):
        User.objects.create(
            username = username,
            password=password ,
            access_token=access_token,
            token_created_at=token_created_at,
            created_at = timezone.now
        )
    def get_user_by_token(self, token):
        user = User.objects.get(access_token = token)
        return user