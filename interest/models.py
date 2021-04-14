from django.db import models
from django.utils.timezone import now
from django.conf import settings

# Create your models here.


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    created_time = models.DateTimeField(default=now)
    last_mod_time = models.DateTimeField(default=now)

    class Meta:
        abstract = True


class InterestOrganization(BaseModel):
    '''兴趣圈'''
    STATUS = (
        ('o', '正常'),
        ('d', '关闭'),
        ('s', '审核中')
    )
    name = models.CharField('兴趣圈名字', max_length=32)
    title = models.TextField('简介')
    status = models.CharField('状态', max_length=1, choices=STATUS, default='s')
    create_account = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       verbose_name='创建者',
                                       related_name='my_organization',
                                       on_delete=models.SET_NULL,
                                       null=True)
    accounts = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                      verbose_name='关注用户',
                                      )


class Article(BaseModel):
    COMMENT_STATUS = (
        ('o', '打开评论'),
        ('c', '关闭评论')
    )
    STATUS = (
        ('o', '正常'),
        ('d', '删除')
    )
    title = models.CharField('标题', max_length=200)
    # body = MDTextField('正文')
    body = models.TextField('正文')
    comment_status = models.CharField('评论状态', max_length=1, choices=COMMENT_STATUS, default='o')
    views = models.PositiveIntegerField('浏览量', default=0)
    fabulous = models.PositiveIntegerField('点赞量', default=0)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='作者', blank=False, null=False,
                               on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', verbose_name='标签集合', blank=True)
    organization = models.ForeignKey('InterestOrganization', verbose_name='所属圈子', on_delete=models.SET_NULL, null=True)
    status = models.CharField('状态', max_length=1, choices=STATUS, default='o')

    def increase_views(self):
        # 增加阅读量
        self.views += 1
        self.save(update_fields=['views'])

    def __str__(self):
        return self.title

class Tag(BaseModel):
    '''标签'''
    name = models.CharField('标签名', max_length=30, unique=True)



