from abc import ABC, abstractmethod
from fb_auth.models import User
class RegisterUserStorageInterface(ABC):
    @abstractmethod
    def register_user(self, username, password, access_token, token_created_at):
        pass
    @abstractmethod
    def get_user_by_token(self, token):
        pass