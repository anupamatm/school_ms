from django.contrib import admin
from django.urls import path
from . import views
app_name='teacher'
urlpatterns = [
    path('t_login',views.t_login,name='t_login'),
    path('t_home',views.t_home,name='t_home'),
    path('add_student',views.add_student,name='add_student'),
    path('tview_profile',views.tview_profile,name='tview_profile'),
    path('tview_student',views.tview_student,name='tview_student'),
    path('tchange_password',views.tchange_pwd,name='tc_pwd')
    
]
