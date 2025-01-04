from django.urls import path
from resume import views as resume_views

urlpatterns = [
    path('', resume_views.home, name='home'),
]