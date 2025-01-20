#管理ツール（superuser）で編集できるものを各アプリのここに記述
from django.contrib import admin  #Djangoの管理サイト機能を提供するモジュール
from django.contrib.auth.admin import UserAdmin  #Djangoの組み込みUserモデルを管理するための標準管理インターフェースを提供
from accounts.models import User


@admin.register(User) #カスタムユーザーモデル（User）をDjangoの管理サイトに登録し、以下のカスタマイズを適用
class CustomUserAdmin(UserAdmin):
    model = User
    # 管理ツール画面のリスト表示で表示するフィールドを指定、管理ツール画面の並びも以下のリストに従う
    list_display = ['id',
                    'username', 
                    'email', 
                    'is_staff', #ユーザーが管理画面（Django Admin）にアクセスできるか権限があるかどうか
                    'is_active',#ユーザーアカウントがアクティブかどうか(ログインできるか否か)
                    'is_superuser'#管理者権限か否か
                ]

