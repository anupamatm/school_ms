from django.contrib import admin
from django.urls import path
from . import views
app_name="school_admin"
urlpatterns = [
   
   path("a_login",views.a_login,name="a_login"),
   path("a_home",views.a_home,name="a_home"),
   path("add_teacher",views.add_teacher,name="add_teacher"),
   path("view_teacher",views.view_teacher,name="view_teacher"),
   path("add_student",views.view_student,name="view_student"),
   path("a_profile",views.a_profile,name="admin_profile"),
   path("c_pwd",views.c_pwd,name="c_pwd"),
   
]
