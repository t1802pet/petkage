from django.conf import settings
from django.db import models
from django.utils import timezone

# from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    photo = models.ImageField('사진',upload_to='post')
    pstdate = models.DateTimeField('작성일', auto_now=True, null=True, blank=True)
    psttext = models.TextField('내용작성',null = False, default ="")

    def __str__(self):
        return f'Post (PK: {self.pk}, Author: {self.author.username})', self.psttext


    class Meta:
        ordering = ['-pk']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()

    def __str__(self):
        return f'Comment (PK: {self.pk}, Author: {self.author.username})'

