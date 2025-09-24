from abc import ABC, abstractmethod
class RegisterUserStorageInterface(ABC):
    @abstractmethod
    def register_user(self, username, password, access_token):
        pass
    @abstractmethod
    def get_user_by_token(self, token):
        pass