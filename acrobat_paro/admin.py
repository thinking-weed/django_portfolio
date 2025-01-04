#管理ツール（superuser）で編集できるものを各アプリのここに記述
from django.contrib import admin
from acrobat_paro.models import Created_PDF

@admin.register(Created_PDF)
class Created_PDF_Admin(admin.ModelAdmin):
    list_display = ['id', 'file_name', 'description', 'file_path', 'created_at', 'updated_at', 'delete_flag']