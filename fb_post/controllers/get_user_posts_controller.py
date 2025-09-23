
from rest_framework.views import APIView
from rest_framework.response import Response
from fb_post.storages.django_get_user_posts_storage import GetUserPostsStorage
from fb_post.interactors.get_user_posts_interactor import GetUserPostsInteractor
from fb_post.presenters.django_get_user_posts_presenter import GetUserPostPresenter
from fb_post.serializers.serializers import PostSerializer

class GetUserPostsController(APIView):
    def get(self, request):
        user = request.user
        user_id = user.id
        interactor = GetUserPostsInteractor(
            storage=GetUserPostsStorage(),
        )
        response_dto_list = interactor.get_user_posts(user_id=user_id)
        serializer = PostSerializer(response_dto_list, many=True)
        return Response(serializer.data)