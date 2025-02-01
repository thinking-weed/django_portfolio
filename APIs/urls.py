from django.urls import path
from APIs import views

app_name = 'APIs'  # 名前空間を設定する

urlpatterns = [
    path('postcode_search/', views.postcode_search, name='postcode_search')
]