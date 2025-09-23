from fb_auth.models import FbUser
from django.utils import timezone
from fb_auth.interactor.storage_interfaces.register_user_storage import RegisterUserStorageInterface
class RegisterUserStorage(RegisterUserStorageInterface):
    def register_user(self, username, password, access_token):
        FbUser.objects.create(
            username = username,
            password=password ,
            access_token=access_token,
            created_at = timezone.now()
        )
    def get_user_by_token(self, token):
        user = FbUser.objects.get(access_token = token)
        return user