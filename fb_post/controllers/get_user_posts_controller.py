
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from fb_post.storages.django_get_user_posts_storage import GetUserPostsStorage
from fb_post.interactors.get_user_posts_interactor import GetUserPostsInteractor
from fb_post.presenters.django_get_user_posts_presenter import GetUserPostsPresenter

class GetUserPostsController(APIView):
    def get(self, request):
        try:
            user = request.user
            user_id = user.id

            post_offset = self._validate_int_param(request.GET.get('post_offset', 0), 'post_offset', min_value=0)
            post_limit = self._validate_int_param(request.GET.get('post_limit', 10), 'post_limit', min_value=1, max_value=100)
            comment_offset = self._validate_int_param(request.GET.get('comment_offset', 0), 'comment_offset', min_value=0)
            comment_limit = self._validate_int_param(request.GET.get('comment_limit', 10), 'comment_limit', min_value=1, max_value=100)
            replies_limit = self._validate_int_param(request.GET.get('replies_limit', 5), 'replies_limit', min_value=1, max_value=50)

            storage = GetUserPostsStorage()
            interactor = GetUserPostsInteractor(storage=storage)
            presenter = GetUserPostsPresenter()

            response_data = interactor.get_user_posts_wrapper(
                user_id=user_id,
                presenter=presenter,
                post_offset=post_offset,
                post_limit=post_limit,
                comment_offset=comment_offset,
                comment_limit=comment_limit,
                replies_limit=replies_limit
            )
            
            return Response(response_data, status=status.HTTP_200_OK)
            
        except ValueError as e:
            return Response(
                {"error": "Invalid parameter", "detail": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            return Response(
                {"error": "Internal server error", "detail": str(e)}, 
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    
    def _validate_int_param(self, value, param_name, min_value=None, max_value=None):

        try:
            int_value = int(value)
            if min_value is not None and int_value < min_value:
                raise ValueError(f"{param_name} must be >= {min_value}")
            if max_value is not None and int_value > max_value:
                raise ValueError(f"{param_name} must be <= {max_value}")
            return int_value
        except (ValueError, TypeError):
            raise ValueError(f"{param_name} must be a valid integer")