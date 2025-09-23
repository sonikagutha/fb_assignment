from django.db import models
from django.utils import timezone
from fb_auth.models import FbUser


class Group(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    content = models.CharField(max_length=1000)
    posted_at = models.DateTimeField(default=timezone.now)
    posted_by = models.ForeignKey(FbUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.posted_by.username} posted {self.content}'


class Comment(models.Model):
    content = models.CharField(max_length=1000)
    commented_at = models.DateTimeField(default=timezone.now)
    commented_by = models.ForeignKey(FbUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.content} is comment for {self.post} by {self.commented_by}'
    # comment_reaction = models.OneToOneField(Comment, choices=react, on_delete=models.CASCADE)


class Reaction(models.Model):
    react = [
        ("WOW", "wow"),
        ("LIT", "lit"),
        ("LOVE", "Love"),
        ("HAHA", "Haha"),
        ("THUMBS-UP", "Thumbs-up"),
        ("THUMPS-DOWN", "Thumps-down"),
        ("ANGRY", "Angry"),
        ("SAD", "Sad")
    ]
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    reaction = models.CharField(max_length=30, choices=react)
    reacted_at = models.DateTimeField(default=timezone.now)
    reacted_by = models.ForeignKey(FbUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.reaction} is reacted by {self.reacted_by} on post {self.post}'

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['reacted_by', 'post'], name='unique_user_post_reaction'),
            models.UniqueConstraint(fields=['reacted_by', 'comment'], name='unique_user_comment_reaction')
        ]


class Membership(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    member = models.ForeignKey(FbUser, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['group', 'member'], name='unique_group_members')
        ]
