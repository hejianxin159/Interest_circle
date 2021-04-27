# -*- coding: utf-8 -*-
# author: hejianxin
# date: 2021/4/10 22:21

from rest_framework import serializers
from interest.models import Article, InterestOrganization, Tag
from account.serializers import AccountsSerializer

class InterestOrganizationSerializer(serializers.Serializer):
    STATUS = (
        ('o', '正常'),
        ('d', '关闭'),
        ('s', '审核中')
    )
    name = serializers.CharField(label='兴趣圈名字', max_length=32)
    title = serializers.CharField(label='简介')
    status = serializers.CharField(label='状态', max_length=1, default='s')
    create_account = AccountsSerializer()


class ArticleSerializer(serializers.Serializer):
    COMMENT_STATUS = (
        ('o', '打开评论'),
        ('c', '关闭评论')
    )
    STATUS = (
        ('o', '正常'),
        ('d', '删除')
    )
    id = serializers.IntegerField(label='id', read_only=True)
    title = serializers.CharField(label='标题', max_length=200)
    # body = MDTextField('正文')
    body = serializers.CharField(label='正文')
    comment_status = serializers.CharField(label='评论状态', max_length=1, default='o')
    views = serializers.IntegerField(label='浏览量', default=0)
    fabulous = serializers.IntegerField(label='点赞量', default=0)
    author = AccountsSerializer()
    organization = InterestOrganizationSerializer()
    status = serializers.CharField(label='状态', max_length=1, default='o')

# class AccountsSerializer(serializers.Serializer):
#     id = serializers.IntegerField(label='id', read_only=True)
#     nick_name = serializers.CharField(label='昵称', max_length=100)
#     real_name = serializers.CharField(label='真实姓名', max_length=32, required=False)
#     email = serializers.EmailField(label='邮箱')
#     id_card = serializers.CharField(label='生份证号', max_length=18, required=False)
#     phone = serializers.CharField(label='电话号码', max_length=32)
#     credit = serializers.IntegerField(label='学分', default=0)
#     title = serializers.CharField(label='荣誉称号', max_length=32, required=False)
#     is_certified = serializers.BooleanField('是否学生认证', default=False)
#     school = SchoolSerializer()
