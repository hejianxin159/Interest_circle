from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now
# Create your models here.


class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('学校名称', max_length=100)
    information = models.TextField('学校简介')


class Accounts(AbstractUser):
    nick_name = models.CharField('昵称', max_length=100, blank=True)
    real_name = models.CharField('真实姓名', max_length=32)
    id_card = models.CharField('生份证号', max_length=18)
    phone = models.CharField('电话号码', max_length=32)
    credit = models.SmallIntegerField('学分', default=0)
    title = models.CharField('荣誉称号', max_length=32)
    is_certified = models.BooleanField('是否学生认证', default=False)
    school = models.ForeignKey('School', verbose_name='作者', null=True,
                               on_delete=models.SET_NULL)
    created_time = models.DateTimeField('创建时间', default=now)
    last_mod_time = models.DateTimeField('修改时间', default=now)

