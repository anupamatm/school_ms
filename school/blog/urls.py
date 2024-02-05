
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
app_name='blog'
urlpatterns = [
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.like_post, name='like_post'),
    path('add_post',views.add_post,name="add_post"),
    path('add_user', views.add_user, name='add_user'),
    path('login', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('blog', views.blog_list, name='blog_list'),
    
]
