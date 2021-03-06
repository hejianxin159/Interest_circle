from django.shortcuts import render, redirect, reverse
from rest_framework.views import APIView
from account.models import School, Accounts
# from django.http import HttpResponse, JsonResponse
from interest_circle.utils.response import JsonResponse
from account.serializers import AccountsSerializer
from rest_framework import generics
from rest_framework import viewsets
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, logout
from django.db.models import Q

class Login(APIView):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        if all([email, password]):
            account = Accounts.objects.filter(email=email).first()
            if not account:
                return JsonResponse({
                    'status': 'fail',
                    'message': '找不到用户'
                }, 406)
            if check_password(password, account.password):
                login(request, account)
                return JsonResponse({
                    'status': 'success',
                    'message': 'success'
                    # 'message': AccountsSerializer(instance=account).data
                })
            else:
                return JsonResponse({
                    'status': 'fail',
                    'message': '密码错误'
                }, 406)
        return JsonResponse({
            'status': 'fail',
            'message': 'error'
        }, 406)


class Register(APIView):

    def get(self, request):
        schools = School.objects.all()
        return render(request, 'register.html', {'schools': schools})

    def post(self, request):
        nick_name = request.POST.get('nick_name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        school = request.POST.get('school')

        exist_account = Accounts.objects.filter(Q(email=email) | Q(username=nick_name)).first()
        if exist_account:
            if exist_account.email == email:
                return JsonResponse({'status': 'fail',
                                     'message': '该邮箱已经注册'},
                                    status=200)
            else:
                return JsonResponse({'status': 'fail',
                                     'message': '该用户已经注册'},
                                    status=200)
        else:
            if all([nick_name, password, email, school]):
                school_obj = School.objects.filter(name=school).first()
                if not school_obj:
                    return JsonResponse({'status': 'fail',
                                         'message': '找不到学校'},
                                        status=200)
                create_account = Accounts.objects.create(
                                    username=nick_name,
                                    email=email,
                                    school=school_obj
                                )
                create_account.set_password(password)
                create_account.save()

                serializer_data = AccountsSerializer(instance=create_account)
                return JsonResponse({'status': 'success',
                                     'message': serializer_data.data},
                                    status=200)

        return JsonResponse({'status': 'fail',
                             'message': 'error'},
                            status=200)


class Logout(APIView):
    def get(self, request):
        logout(request)
        return JsonResponse({'status': 'success',
                             'message': '退出成功'})
