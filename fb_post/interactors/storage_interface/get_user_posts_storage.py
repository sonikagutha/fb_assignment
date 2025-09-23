
from abc import ABC, abstractmethod
from typing import List
from fb_post.models import Post, Comment, Reaction

class GetUserPostsStorageInterface(ABC):

    @abstractmethod
    def get_posts_by_user_id(self, user_id: int, offset: int = 0, limit: int = 10) -> List[Post]:
        """Fetch posts for a user with pagination"""
        pass

    @abstractmethod
    def get_reactions_for_post(self, post: Post) -> List[Reaction]:
        pass

    @abstractmethod
    def get_reactions_for_comment(self, comment: Comment) -> List[Reaction]:
        pass

    @abstractmethod
    def get_comments_for_post(self, post: Post, offset: int = 0, limit: int = 10) -> List[Comment]:
        """Fetch top-level comments for a post with pagination"""
        pass

    @abstractmethod
    def get_replies_for_comment(self, comment: Comment, offset: int = 0, limit: int = 5) -> List[Comment]:
        """Fetch replies for a comment with pagination"""
        pass