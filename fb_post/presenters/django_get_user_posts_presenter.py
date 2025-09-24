from typing import List
from fb_post.dtos import PostDTO, CommentDTO

class GetUserPostsPresenter:
    def get_user_posts_response(self, posts: List[PostDTO]):
        return [self._post_to_dict(post) for post in posts]

    def _post_to_dict(self, post: PostDTO):
        return {
            "post_id": post.post_id,
            "group": self._group_to_dict(post.group),
            "posted_by": self._user_to_dict(post.posted_by),
            "posted_at": post.posted_at,
            "post_content": post.post_content,
            "reactions": self._reaction_to_dict(post.reactions),
            "comments": [self._comment_to_dict(c) for c in post.comments],
            "comments_count": post.comments_count
        }

    def _group_to_dict(self, group):
        if not group:
            return None
        return {
            "group_id": group.group_id,
            "name": group.name
        }

    def _user_to_dict(self, user):
        return {
            "user_id": user.user_id,
            "name": user.name,
            "profile_pic": user.profile_pic
        }

    def _reaction_to_dict(self, reaction):
        return {
            "count": reaction.count,
            "types": reaction.types
        }

    def _comment_to_dict(self, comment: CommentDTO):
        return {
            "comment_id": comment.comment_id,
            "commenter": self._user_to_dict(comment.commenter),
            "commented_at": comment.commented_at,
            "comment_content": comment.comment_content,
            "reactions": self._reaction_to_dict(comment.reactions),
            "replies_count": comment.replies_count,
            "replies": [self._comment_to_dict(r) for r in comment.replies]
        }
