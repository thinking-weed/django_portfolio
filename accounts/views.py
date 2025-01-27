from django.shortcuts import render
from django.http import HttpResponse
from accounts.models import User
from accounts.forms import CheckedUserForm
from django.db.models import QuerySet 
#Djangoでall()を使ったときに取り出されるクエリ取得用にいろいろ機能拡張したセット

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

def users_index_values_list(request):
    userdatas = User.objects.all().order_by('id').values_list('id','username','email')
    params = { #.values_listで取り出したモデルをリストとして取り出す
        'title':'Hello',
        'userdatas':userdatas
    }
    return render(request, 'accounts/all_users_values.html', params)

def first_last_counts_get(request):
    first = User.objects.all().first() #allなどで得られたレコードの内、最初のものだけ返す
    last = User.objects.all().last() #allなどで得られたレコードの内、最後のものだけ返す
    num = User.objects.all().count() #取得したレコード数を返す
    # 特定のカラムの値を取得
    first_name = first.username if first else None  # 'name' フィールドの値（存在しない場合はNone）
    last_email = last.email if last else None  # 'email' フィールドの値（存在しない場合はNone）

    userdatas = [num, first_name, last_email]

    params = {
        'title':'Hello',
        'userdatas':userdatas
    }
    return render(request, 'accounts/all_users_values.html', params)

#Querysetの機能の一部書き換え
def __new__str__(self):
    result = ''
    for item in self:
        result += '<tr>'
        for k in item:
            result += '<td>' + str(k) + '=' + str(item[k]) + '</td>'
        result += '</tr>'
    return result

QuerySet.__str__ = __new__str__ #左辺の__str__はmodels.pyで定義しているものと思われる

def customize_queryset(request):
    userdata = User.objects.all().order_by('id').values('id','username','email')
    params = { #.values_listで取り出したモデルをリストとして取り出す
        'title':'Hello',
        'userdata':userdata
    }
    return render(request, 'accounts/customize_queryset.html', params)
