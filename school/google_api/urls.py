from django.contrib import admin
from django.urls import path
from . import views
app_name='google_api'
urlpatterns = [
    path('index',views.index,name='index'),
    path('get_meals', views.get_meals, name = "get_meals"),
    path('meals/<int:id>',views.meal_detail, name = "meal_detail")
    
]
