from abc import ABC, abstractmethod
from typing import List
from fb_post.dtos import PostDTO
class GetUserPostsPresenterInterface(ABC):
    @abstractmethod
    def get_user_posts_response(self, posts: List[PostDTO]):
        pass
