# -*- coding: utf-8 -*-
# author: hejianxin
# date: 2021/5/5 16:17

from django.http import HttpResponse
import json


def JsonResponse(content, status_code=200):
    if not isinstance(content, dict):
        assert TypeError('content must json')
    content = json.dumps(content)
    response = HttpResponse()
    response.content = content
    response.status_code = status_code
    return response