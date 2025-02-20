from django.urls import path
from APIs import views
from APIs import typehints_sample1,typehints_sample2,typehints_sample3

app_name = 'APIs'  # 名前空間を設定する
#prefixは/apis/

urlpatterns = [
    path('postcode_search/', views.postcode_search, name='postcode_search'),
    path('typehints_sample1/', views.typehints_sample1, name='typehints_sample1'),
    path('typehints_sample2/', views.typehints_sample2, name='typehints_sample2'),
    path('typehints_sample3/', views.typehints_sample3, name='typehints_sample3')

]