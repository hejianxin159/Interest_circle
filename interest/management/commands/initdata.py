# -*- coding: utf-8 -*-
# author: hejianxin
# date: 2021/4/8 22:26

from django.core.management.base import BaseCommand, CommandError
from account.models import Accounts, School
from interest.models import InterestOrganization, Tag, Article


class Command(BaseCommand):
    def handle(self, *args, **options):

        school = School.objects.create(name='乐山职业技术学院', information='asfasfasdfs')
        account = Accounts.objects.create_user(username='he1111211jx', password='123', email='18121319056008@qq.com', school=school)
        tag = Tag.objects.create(name='学2习1111111111')
        organization = InterestOrganization.objects.create(
            name='python俱乐部',
            title='欢迎大佬们常驻',
            create_account=account
        )
        for i in range(100):
            article = Article.objects.create(
                title='python学习路线',
                body='python学习路线之学习路线python学习路线之学习路线python学习路线之学习路线python学习路线之学习路线',
                views=20,
                fabulous=5,
                author=account,
                organization=organization
            )
            article.tags.add(tag)