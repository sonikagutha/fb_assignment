from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone


class FbUser(AbstractUser):

    username = models.CharField(max_length=50, unique=True, null=True)
    access_token = models.CharField(max_length=100, blank=True, null=True)
    token_created_at = models.DateTimeField(blank=True, null=True)
    profile_pic = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        Group,
        related_name="fbuser_groups",
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="fbuser_permissions",
        blank=True,
    )

    def __str__(self):
        return self.username
