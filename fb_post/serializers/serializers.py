from rest_framework import serializers

class UserSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    name = serializers.CharField()
    profile_pic = serializers.URLField(allow_null=True, required=False)

class ReactionSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    types = serializers.ListField(child=serializers.CharField())

class ReplySerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    commenter = UserSerializer()
    commented_at = serializers.CharField()
    comment_content = serializers.CharField()
    reactions = ReactionSerializer()

class CommentSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    commenter = UserSerializer()
    commented_at = serializers.CharField()
    comment_content = serializers.CharField()
    reactions = ReactionSerializer()
    replies_count = serializers.IntegerField()
    replies = ReplySerializer(many=True)

class GroupSerializer(serializers.Serializer):
    group_id = serializers.IntegerField()
    name = serializers.CharField()

class PostSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    group = GroupSerializer(allow_null=True)
    posted_by = UserSerializer()
    posted_at = serializers.CharField()
    post_content = serializers.CharField()
    reactions = ReactionSerializer()
    comments = CommentSerializer(many=True)
    comments_count = serializers.IntegerField()
