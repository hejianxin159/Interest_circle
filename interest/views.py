from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.pagination import PageNumberPagination
from interest.serializers import InterestOrganizationSerializer, ArticleSerializer
from rest_framework.views import APIView
from interest.models import InterestOrganization, Tag, Article
from django.utils.timezone import now
from datetime import timedelta
from django_redis import get_redis_connection
import json
# Create your views here.


conn = get_redis_connection('default')


class Index(APIView):
    def get(self, request):
        # keyword = request.query_params.get('keyword')
        # if keyword == 'hot':
        #     # 热门兴趣， 查询当前7天数据，按照点赞数量排序
        #     article_list = Article.objects.filter(created_time__gte=now() + timedelta(days=-7)).order_by('views')
        #     # for i in article_list:
        #     #     print(i)
        #     # 创建分页对象
        #     pager = PageNumberPagination()
        #     pager_data = pager.paginate_queryset(queryset=article_list, request=request)
        #     serializer_data = ArticleSerializer(pager_data, many=True)
        #     return pager.get_paginated_response(serializer_data.data)
        #     # return JsonResponse(json.dumps(serializer_data.data, ensure_ascii=True))
        #     # return JsonResponse(pager.get_paginated_response(serializer_data.data))
        #     # return JsonResponse(serializer_data.data)
        #
        # user = request.user

        return render(request, 'index.html')


class IndexArticle(APIView):
    def get(self, request):
        keyword = request.query_params.get('keyword')
        # 创建分页对象
        pager = PageNumberPagination()
        if keyword == 'hot':
            # 热门兴趣， 查询当前7天数据，按照点赞数量排序
            article_list = Article.objects.filter(created_time__gte=now() + timedelta(days=-7)).order_by('views')
            pager_data = pager.paginate_queryset(queryset=article_list, request=request)
            serializer_data = ArticleSerializer(pager_data, many=True)
        else:
            article_list = Article.objects.all().order_by('views')
            pager_data = pager.paginate_queryset(queryset=article_list, request=request)
            serializer_data = ArticleSerializer(pager_data, many=True)
        return pager.get_paginated_response(serializer_data.data)


