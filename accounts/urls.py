from django.urls import path
from accounts import views as accounts_views

app_name = 'accounts'  # 名前空間を設定する

urlpatterns = [
    path('all_users/', accounts_views.users_index, name='all_users'),
    path('checked_users/', accounts_views.checked_index, name='checked_index'),
    path('all_users_list/' ,accounts_views.users_index_list, name='users_index_list'),
    path('all_users_values/' ,accounts_views.users_index_values, name='users_index_values')
]