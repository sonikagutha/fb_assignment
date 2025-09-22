import uuid
from django.utils import timezone
def generate_token():
    return str(uuid.uuid4()), timezone.now
class RegisterUserInteractor:
    def __init__(self, storage):
        self.storage = storage
    def register(self, username, password):
        token, token_created_at = generate_token()
        self.storage.register_user(username, password, token, token_created_at)
        return {"User registered successfully"}
    def validate_token(self, token):
        user = self.storage.get_user_by_token(token)
        if not user:
            return None
        return user.access_token