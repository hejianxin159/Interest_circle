# -*- coding: utf-8 -*-
# Author : hejianxin
# Time : 2021/3/29 2:40 下午
from django.urls import path
from interest import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('article', views.IndexArticle.as_view(), name='article')
]
