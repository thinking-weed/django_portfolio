from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User

from django_portfolio import settings

#prefixのURLは「accounts/」

def users_index(request):
    userdatas = User.objects.all() #Userの全レコードを取得する
    params = {
        'userdatas':userdatas
    }
    return render(request, 'accounts/users.html', params)
