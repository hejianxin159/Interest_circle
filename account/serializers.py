# -*- coding: utf-8 -*-
# Author : hejianxin
# Time : 2021/3/30 4:27 下午

import django
django.setup()
from account.models import Accounts
from account.models import School
from rest_framework import serializers


class SchoolSerializer(serializers.Serializer):
    name = serializers.CharField(label='学校名称', max_length=100)
    information = serializers.CharField(label='学校简介')


class AccountsSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='id', read_only=True)
    nick_name = serializers.CharField(label='昵称', max_length=100)
    real_name = serializers.CharField(label='真实姓名', max_length=32, required=False)
    email = serializers.EmailField(label='邮箱')
    id_card = serializers.CharField(label='生份证号', max_length=18, required=False)
    phone = serializers.CharField(label='电话号码', max_length=32)
    credit = serializers.IntegerField(label='学分', default=0)
    title = serializers.CharField(label='荣誉称号', max_length=32, required=False)
    is_certified = serializers.BooleanField('是否学生认证', default=False)
    school = SchoolSerializer()

    # class Meta:
    #     model = Accounts
    #     fields = ('nick_name', 'real_name', 'id_card', 'phone', 'credit', 'title', 'is_certified', 'school')

