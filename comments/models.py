from django.db import models
from django.conf import settings
from interest.models import Article
from django.utils.timezone import now

# Create your models here.


class Comment(models.Model):
    '''评论'''
    STATUS = (
        ('o', '正常'),
        ('d', '删除')
    )
    body = models.CharField('评论内容', max_length=200)
    account = models.ForeignKey(settings.AUTH_USER_MODEL,
                                verbose_name='评论人',
                                on_delete=models.SET_NULL,
                                null=True)
    article = models.ForeignKey(Article,
                                verbose_name='文章',
                                on_delete=models.SET_NULL,
                                null=True)
    parent_comment = models.ForeignKey('self',
                                       verbose_name='上级评论',
                                       on_delete=models.SET_NULL,
                                       null=True)
    status = models.CharField('状态',
                              max_length=1,
                              choices=STATUS,
                              default='o')

    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)


class Support(models.Model):
    '''点赞功能'''
    user_id = models.IntegerField('用户id', db_index=True)
    article_id = models.IntegerField('文章id', db_index=True)
