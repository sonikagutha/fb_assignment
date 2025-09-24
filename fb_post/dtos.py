from dataclasses import dataclass
from typing import List, Optional

@dataclass
class UserDTO:
    user_id: int
    name: str
    profile_pic: Optional[str]

@dataclass
class GroupDTO:
    group_id: int
    name: str

@dataclass
class ReactionDTO:
    count: int
    types: List[str]

@dataclass
class CommentDTO:
    comment_id: int
    commenter: UserDTO
    commented_at: str
    comment_content: str
    reactions: ReactionDTO
    replies_count: int
    replies: List["CommentDTO"]

@dataclass
class PostDTO:
    post_id: int
    posted_by: UserDTO
    group: Optional[GroupDTO]
    posted_at: str
    post_content: str
    reactions: ReactionDTO
    comments: List[CommentDTO]
    comments_count: int
