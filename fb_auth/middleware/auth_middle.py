# fb_auth/middleware/auth_middleware.py
from django.http import JsonResponse
from fb_auth.interactor.register_user_interactor import RegisterUserInteractor
from fb_auth.storage.django_register_user_storage import RegisterUserStorage
class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        token = request.headers.get("token")
        if not token:
            return JsonResponse({"error": "Authentication token required"}, status=401)
        try:
            interactor = RegisterUserInteractor(storage=RegisterUserStorage())
            user_token = interactor.validate_token(token)
            if not user_token:
                return JsonResponse({"error": "Invalid or expired token"}, status=401)
            request.user = interactor.storage.get_user_by_token(token)
        except Exception as e:
            return JsonResponse({"error": "Authentication failed", "detail": str(e)}, status=401)
        return self.get_response(request)
