from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User
from accounts.forms import CheckedUserForm
from django_portfolio import settings

#prefixのURLは「accounts/」

def users_index(request):
    userdatas = User.objects.all() #Userの全レコードを取得する
    params = {
        'userdatas':userdatas
    }
    return render(request, 'accounts/all_users.html', params)

def checked_index(request):
    params = {
        'title':'Hello',
        'message':'checked users',
        'form':CheckedUserForm(),
        'userdatas':[]
    }
    if (request.method == 'POST'):
        num = request.POST['id']
        item = User.objects.get(id=num)
        params['userdatas'] = [item]
        params['form'] = CheckedUserForm(request.POST)
    else:
        params['userdatas'] = User.objects.all()
    return render(request, 'accounts/checked_users.html', params)

def users_index_list(request):
    userdatas = User.objects.all() #Userの全レコードを取得する
    params = {
        'title':'Hello',
        'userdatas':userdatas
    }
    return render(request, 'accounts/all_users_list.html', params)


def users_index_values(request):
    userdatas = User.objects.all().order_by('id').values('id','username') #all()でモデルのインスタンスを全て取り出して、そこからレコードの値だけ辞書形式で取得
    #valuesに引数（migrationファイルを参照）を（複数）書くことでその項目の値だけ取得
    #降順で取得する場合はuserdatas = User.objects.all().order_by('-id').values('id', 'username')
    params = {
        'title':'Hello',
        'userdatas':userdatas
    }
    return render(request, 'accounts/all_users_values.html', params)