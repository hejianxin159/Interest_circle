# -*- coding: utf-8 -*-
# Author : hejianxin
# Time : 2021/3/30 4:19 下午
from django.urls import path
from account import views


urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('register', views.Register.as_view(), name='register'),

]