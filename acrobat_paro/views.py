from django.shortcuts import render
from django.http import HttpResponse
from django_portfolio import settings

#prefixのURLは「acrobat_paro/」

pdf_url_prefix = settings.MEDIA_ROOT
def menu_show(request):
    params = {
        'pdf_url_prefix':pdf_url_prefix
    }
    return render(request, 'acrobat_paro/menu.html', params)


