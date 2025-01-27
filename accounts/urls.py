from django.urls import path
from accounts import views as accounts_views

app_name = 'accounts'  # 名前空間を設定する

urlpatterns = [
    path('all_users/', accounts_views.users_index, name='all_users'),
    path('checked_users/', accounts_views.checked_index, name='checked_index'),
    path('all_users_list/' ,accounts_views.users_index_list, name='users_index_list'),
    path('all_users_values/' ,accounts_views.users_index_values, name='users_index_values'),
    path('all_users_values_list/' ,accounts_views.users_index_values_list, name='users_index_values_list'),
    path('first_last_counts_get/' , accounts_views.first_last_counts_get, name='first_last_counts_get'),
    path('customize_queryset/' ,accounts_views.customize_queryset, name='customize_queryset')
]