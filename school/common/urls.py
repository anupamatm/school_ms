from django.contrib import admin
from django.urls import path
from . import views
app_name='common'
urlpatterns = [
    path('',views.home,name='home'),
    path("chart",views.chart,name="chart")
    
]
