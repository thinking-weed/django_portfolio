from django.urls import path
from acrobat_paro import views as acrobat_paro_views

app_name = 'acrobat_paro'  # 名前空間を設定する

urlpatterns = [
    path('', acrobat_paro_views.menu_show, name='menu_show'),
    path('users/', acrobat_paro_views.users_index, name='users_index')
]