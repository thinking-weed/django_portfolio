from django.urls import path
from APIs import views
from APIs import typehints_sample

app_name = 'APIs'  # 名前空間を設定する

urlpatterns = [
    path('postcode_search/', views.postcode_search, name='postcode_search'),
    path('typehints_sample/', views.typehints_sample, name='typehints_sample')
]