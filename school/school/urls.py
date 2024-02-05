"""school URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('common.urls')),
    path('school_admin/',include('school_admin.urls')),
    path('student/',include('student.urls')),
    path('teacher/',include('teacher.urls')),
    path('student_api/',include('student_api.urls')),
    path('google_api/',include('google_api.urls')),
    path('student_fend/',include('student_fend.urls')),
    (path('blog/',include('blog.urls')))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
