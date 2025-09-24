from typing import List
from fb_post.dtos import UserDTO, GroupDTO, ReactionDTO, CommentDTO, PostDTO
from fb_post.models import Post, Comment, Group
from fb_auth.models import FbUser
from fb_post.interactors.storage_interface.get_user_posts_storage import GetUserPostsStorageInterface
from fb_post.interactors.presenter_interface.get_user_posts_presenter import GetUserPostsPresenterInterface

class GetUserPostsInteractor:

    def __init__(self, storage: GetUserPostsStorageInterface):
        self.storage = storage

    def get_user_posts_wrapper(
        self,
        user_id: int,
        presenter: GetUserPostsPresenterInterface,
        post_offset: int = 0,
        post_limit: int = 10,
        comment_offset: int = 0,
        comment_limit: int = 10,
        replies_limit: int = 5
    ):
        posts_dto = self.get_user_posts(
            user_id=user_id,
            post_offset=post_offset,
            post_limit=post_limit,
            comment_offset=comment_offset,
            comment_limit=comment_limit,
            replies_limit=replies_limit
        )
        return presenter.get_user_posts_response(posts=posts_dto)

    def get_user_posts(
        self,
        user_id: int,
        post_offset: int = 0,
        post_limit: int = 10,
        comment_offset: int = 0,
        comment_limit: int = 10,
        replies_limit: int = 5
    ) -> List[PostDTO]:
        posts = self.storage.get_posts_by_user_id(user_id, offset=post_offset, limit=post_limit)
        # POST DTO
        # Pick post ids
        # send post ids to storage and get the comments -> CommentDTO
        # get comment ids from comment dto and get the replies - CommentDTO


        return [self._get_post_dto(post, comment_offset, comment_limit, replies_limit) for post in posts]

    def _get_user_dto(self, user: FbUser) -> UserDTO:
        return UserDTO(
            user_id=user.id,
            name=user.username,
            profile_pic=user.profile_pic
        )

    def _get_group_dto(self, group: Group) -> GroupDTO:
        if not group:
            return None
        return GroupDTO(
            group_id=group.id,
            name=group.name
        )

    def _get_reaction_dto(self, post: Post = None, comment: Comment = None) -> ReactionDTO:
        reactions = self.storage.get_reactions_for_post(post) if post else self.storage.get_reactions_for_comment(comment)
        return ReactionDTO(
            count=len(reactions),
            types=list(set(r.reaction for r in reactions))
        )

    def _get_post_dto(self, post: Post, comment_offset: int, comment_limit: int, replies_limit: int) -> PostDTO:
        user_dto = self._get_user_dto(post.posted_by)
        group_dto = self._get_group_dto(post.group)
        reactions_dto = self._get_reaction_dto(post=post)
        comment_dtos = self._get_comments_by_post(post, comment_offset, comment_limit, replies_limit)

        return PostDTO(
            post_id=post.id,
            posted_by=user_dto,
            group=group_dto,
            posted_at=str(post.posted_at),
            post_content=post.content,
            reactions=reactions_dto,
            comments=comment_dtos,
            comments_count=len(comment_dtos)
        )

    def _get_comments_by_post(self, post: Post, comment_offset: int, comment_limit: int, replies_limit: int) -> List[CommentDTO]:
        comments = self.storage.get_comments_for_post(post, offset=comment_offset, limit=comment_limit)
        return [self._get_comment_dto(comment, replies_limit) for comment in comments]

    def _get_comment_dto(self, comment: Comment, replies_limit: int) -> CommentDTO:
        commenter_dto = self._get_user_dto(comment.commented_by)
        reactions_dto = self._get_reaction_dto(comment=comment)

        replies = self.storage.get_replies_for_comment(comment, limit=replies_limit)
        reply_dtos = [self._get_comment_dto(reply, replies_limit) for reply in replies]

        return CommentDTO(
            comment_id=comment.id,
            commenter=commenter_dto,
            commented_at=str(comment.commented_at),
            comment_content=comment.content,
            reactions=reactions_dto,
            replies_count=len(reply_dtos),
            replies=reply_dtos
        )