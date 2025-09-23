from typing import List
from fb_post.models import Post, Comment, Reaction
from fb_post.interactors.storage_interface.get_user_posts_storage import GetUserPostsStorageInterface

class GetUserPostsStorage(GetUserPostsStorageInterface):

    def get_posts_by_user_id(self, user_id: int, offset: int = 0, limit: int = 3) -> List[Post]:
        return list(
            Post.objects.filter(posted_by_id=user_id)
            .select_related("posted_by", "group")
            .order_by("-posted_at")[offset:offset + limit]
        )

    def get_reactions_for_post(self, post: Post) -> List[Reaction]:
        return list(Reaction.objects.filter(post=post))

    def get_reactions_for_comment(self, comment: Comment) -> List[Reaction]:
        return list(Reaction.objects.filter(comment=comment))

    def get_comments_for_post(self, post: Post, offset: int = 0, limit: int = 3) -> List[Comment]:
        return list(
            Comment.objects.filter(post=post, parent_comment__isnull=True)
            .select_related("commented_by")
            .order_by("-commented_at")[offset:offset + limit]
        )

    def get_replies_for_comment(self, comment: Comment, offset: int = 0, limit: int = 4) -> List[Comment]:
        return list(
            Comment.objects.filter(parent_comment=comment)
            .select_related("commented_by")
            .order_by("commented_at")[offset:offset + limit]
        )