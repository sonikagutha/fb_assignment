from django.db import models
from django.utils import timezone
class User(models.Model):
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=50)
    access_token = models.CharField(max_length=100, blank=True, null=True)
    token_created_at  = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    profile_pic = models.URLField(null=True,blank=True)