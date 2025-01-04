#どのアドレスにアクセスしたら実行するように、このファイルに追記

"""django_portfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

#pathは、path( アクセスするアドレス, 呼び出す処理 )
urlpatterns = [
    path('admin/', admin.site.urls),
    path('form_components/', include('form_components.urls')),
    path('crud_components/', include('crud_components.urls')),
    #includeという関数は、引数に指定したモジュールを読み込む
    #これで、component内のアドレス割り当ては、すべてcomponentフォルダ内にあるurls.pyに任せることができる
    #/component/というのがprefixのようになっている状態
    #/component/sample1/というエンドポイントを作成するときは、componentフォルダ内にあるurls.pyに 'sample1/'というのを設定する
    path('was_works/', include('was_works.urls')),
    path('acrobat_paro/', include('acrobat_paro.urls')),
    path('', include('resume.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)