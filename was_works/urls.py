from django.urls import path
from was_works import views as was_works_views

app_name = 'was_works'  # 名前空間を設定する

urlpatterns = [
    path('', was_works_views.show, name='was_works_show'),
]