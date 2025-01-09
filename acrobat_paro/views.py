from django.shortcuts import render
from django.http import HttpResponse
from acrobat_paro.models import Created_PDF,User,Partner_Company

from django_portfolio import settings

#prefixのURLは「acrobat_paro/」

pdf_url_prefix = settings.MEDIA_ROOT
def menu_show(request):
    params = {
        'pdf_url_prefix':pdf_url_prefix
    }
    return render(request, 'acrobat_paro/menu.html', params)

def users_index(request):
    userdatas = User.objects.all() #Userの全レコードを取得する
    params = {
        'userdatas':userdatas
    }
    return render(request, 'acrobat_paro/users.html', params)