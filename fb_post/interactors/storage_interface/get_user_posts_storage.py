from abc import ABC, abstractmethod
class GetUserStorageInterface(ABC):
    @abstractmethod
    def get_user_id(self, token):
        pass
    @abstractmethod
    def get_user_posts(self, user_id):
        pass