from django.contrib import admin
from django.urls import path
from . import views
app_name="student"
urlpatterns = [
   path("s_login",views.s_login,name="s_login"),
   path("s_profile",views.s_profile,name="sview_profile"),
   path("s_home",views.student_home,name="s_home"),
   path("s_chane_pwd",views.schange_password,name="s_change_pwd"),
]
