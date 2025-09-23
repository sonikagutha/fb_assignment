# from rest_framework.views import APIView
# from rest_framework.response import Response
# from fb_auth.interactor.register_user_interactor import RegisterUserInteractor
# from fb_auth.storage.django_register_user_storage import RegisterUserStorage
#
# class RegisterController(APIView):
#     def register_controller(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")
#         storage = RegisterUserStorage()
#
#         interactor = RegisterUserInteractor(storage=storage)
#         response_data = interactor.register(username=username, password=password)
#
#         return Response(response_data, status=200)