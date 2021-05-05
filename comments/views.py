from django.shortcuts import render
from rest_framework.views import APIView
from comments.models import Support
# Create your views here.


class SupportArticle(APIView):
    # def get(self, request):
    #     pass

    def post(self, request):
        user_id = request.user.id