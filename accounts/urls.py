from django.urls import path
from accounts import views as accounts_views

app_name = 'accounts'  # 名前空間を設定する

urlpatterns = [
    path('users/index/', accounts_views.users_index, name='users_index')
]