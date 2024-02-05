from django.urls import path
from . import views

urlpatterns = [
    path('load_student',views.load_student,name="l_student"),
    path('add_student',views.add_student,name='add_student'),
    path('del_student/<int:s_id>',views.del_student,name='del_student'),
    path('update_student/<int:s_id>',views.update_student,name='update_student'),
    path('index',views.index,name='index'),
    path('number',views.number,name='number'),
    path('signup',views.signup,name='signup'),
    path('home',views.home,name='home')
    
]