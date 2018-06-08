from django.db import models
from django.conf import settings
from django.utils import timezone

#  게시글 테이블
class HW_Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    psttitle = models.CharField('제목',max_length=30, null = False)
    psttext = models.TextField('내용',null = False)
    pstdate = models.DateTimeField('작성일',auto_now=True)
    bphoto = models.ImageField('사진등록',upload_to='post', null = True, blank=True)


    def __str__(self):
        return f'HW_Post (PK: {self.pk}, Author: {self.author.username})'

    def publish(self):
        self.save()


    def __str__(self):
        return self.psttitle

    class Meta:
        ordering = ['-pk']

class HW_Comment(models.Model):
    post = models.ForeignKey(HW_Post, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField()

    def __str__(self):
        return f'HW_Comment (PK: {self.pk}, Author: {self.author.username})'
