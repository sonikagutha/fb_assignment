from django.urls import path
from fb_post.controllers.get_user_posts_controller import GetUserPostsController

urlpatterns=[
    path("posts/user/", GetUserPostsController.as_view(), name="get_user_posts")
]