from django.contrib import admin
from django.contrib import admin
from fb_post.models import Post, Comment, Reaction, Group
from fb_auth.models import FbUser
admin.site.register(FbUser)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Reaction)
admin.site.register(Group)
# Register your models here.
