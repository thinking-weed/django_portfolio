from django.urls import path
from form_components import views as component_views
from form_components.views import BSFormview,Checkboxform,Pulldown,SessionView

urlpatterns = [
    path('next_sample3/', component_views.next_sample3,name='next_sample3'),
    path('<int:id>/<nickname>/', component_views.sample1, name='sample1'),
    path('sample2/my_name_is_<nickname>.I_am_<int:age>_years_old.', component_views.sample2, name='sample2'),
    path('', component_views.sample3, name='sample3'),
    path('form_input/', component_views.form_input, name='form_input'),
    path('form_response/', component_views.form_response, name='form_response'),
    path('classform/' , component_views.form_by_FormClass, name='form_by_FormClass'),
    path('bs_form/' , component_views.bs_form, name='bs_form'),
    path('form_by_Class/', BSFormview.as_view(), name='form_by_Class'),
    path('checkbox/', Checkboxform.as_view(), name='checkbox'),
    path('pulldown/', Pulldown.as_view(), name='pulldown'),
    path('session/', SessionView.as_view(), name='session_get')
]