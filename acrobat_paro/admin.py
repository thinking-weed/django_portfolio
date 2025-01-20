#管理ツール（superuser）で編集できるものを各アプリのここに記述
from django.contrib import admin  #Djangoの管理サイト機能を提供するモジュール
from acrobat_paro.models import Created_PDF,Partner_Company


@admin.register(Created_PDF) #Created_PDFモデルをDjangoの管理サイトに登録し、以下のカスタマイズを適用
class Created_PDF_Admin(admin.ModelAdmin):
    # 管理ツール画面のリスト表示で表示するフィールドを指定
    list_display = ['id', 'file_name', 'description', 'file_path', 'created_at', 'updated_at', 'delete_flag']

admin.site.register(Partner_Company)
# admin.site.registerは管理ツールに登録するメソッド
