"""MyProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as studentViews


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='myStudent/index.html'), name='studentLogin'),
    path('home/', studentViews.student_home, name='studentHome'),
    path('student-mid1/', studentViews.student_mid1, name='studentMid1'),
    path('student-mid2/', studentViews.student_mid2, name='studentMid2'),
    path('student-sem/', studentViews.student_sem1, name='studentSem'),
    path('student-attendance/', studentViews.student_attendance, name='studentAttendance'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myStudent/logout.html'), name='studentLogout'),

]
