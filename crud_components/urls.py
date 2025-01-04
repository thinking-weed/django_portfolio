from django.urls import path
from crud_components import views as crud_components_views

urlpatterns = [
    path('', crud_components_views.index, name='index'),
]